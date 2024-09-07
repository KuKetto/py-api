"""This module tests the calc handler by simulating HTTP requests"""

from fastapi.testclient import TestClient
from src.main import app
from src.handlers.item import MAX_ITEMS

client = TestClient(app)

class TestItemsCRUD:
    """Test items CRUD operations"""
    def test_item_addition(self):
        """Test item addition"""
        response = client.post("/items",
                               json={"item_name": "chips",
                                     "item_price": 10,
                                     "item_stock": 4})
        assert response.status_code == 200
        assert response.json() == {"success": "The item chips has been stored."}

        response = client.get("/items")
        assert response.status_code == 200
        stored_item = response.json()["items"][0]
        assert stored_item["item_name"] == "chips"
        assert stored_item["item_price"] == 10
        assert stored_item["item_stock"] == 4
        client.delete("/items/all")

    def test_item_addition_overload(self):
        """Test if server responds with 507 when it reaches maximum capacity"""
        for _ in range(MAX_ITEMS):
            response = client.post("/items",
                                   json={"item_name": "chips",
                                         "item_price": 10,
                                         "item_stock": 4})
            assert response.status_code == 200

        response = client.post("/items",
                               json={"item_name": "chips2",
                                     "item_price": 11,
                                     "item_stock": 4})

        assert response.status_code == 507
        assert response.json() == {"detail": "Server can't store more " \
                                             "than " + str(MAX_ITEMS) + " items " \
                                             "at once. Delete an item first " \
                                             "to store this one."}
        client.delete("/items/all")

    def test_item_removal(self):
        """Test item removal"""
        client.post("/items",
                    json={"item_name": "chips",
                          "item_price": 10,
                          "item_stock": 4})

        response = client.get("/items")
        assert response.status_code == 200
        item_delete_uri = "/items/?item_to_be_removed=" + response.json()["items"][0]["item_id"]

        response = client.delete(item_delete_uri)
        assert response.status_code == 200
        assert response.json() == {"success": "The item chips has been removed."}

        response = client.get("/items")
        assert response.status_code == 200
        assert response.json()["items"] == []

    def test_item_update(self):
        """Test item update"""
        client.post("/items",
                    json={"item_name": "chips",
                          "item_price": 10,
                          "item_stock": 4})

        response = client.get("/items")
        assert response.status_code == 200
        item_id = response.json()["items"][0]["item_id"]

        response = client.put("/items",
                              json = {"item_id": item_id,
                                      "item_name": "updated_chips",
                                      "item_price": 20,
                                      "item_stock": 2})
        assert response.status_code == 200
        assert response.json() == {"success": "The item chips has been updated."}

        response = client.get("/items")
        assert response.status_code == 200
        stored_item = response.json()["items"][0]
        assert stored_item["item_name"] == "updated_chips"
        assert stored_item["item_price"] == 20
        assert stored_item["item_stock"] == 2
        client.delete("/items/all")

    def test_invalid_item_ids(self):
        """Test delete and put methods with invalid item ids"""
        client.post("/items",
                    json={"item_name": "chips",
                          "item_price": 10,
                          "item_stock": 4})

        response = client.delete("/items/?item_to_be_removed=test_id")
        assert response.status_code == 400
        assert response.json() == {"detail": "No item with the given "\
                                             "item id is present."}

        response = client.put("/items",
                              json = {"item_id": "test_id",
                                      "item_name": "updated_chips",
                                      "item_price": 10,
                                      "item_stock": 4})

        assert response.status_code == 400
        assert response.json() == {"detail": "No item with the given "\
                                             "item id is present."}

        client.delete("/items/all")
