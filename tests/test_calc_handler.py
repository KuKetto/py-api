"""This module tests the calc handler by sending HTTP request"""

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

class TestSum:
    """Test sum handler function"""
    def test_invalid_input(self):
        """test invalid input, when the request has invalid characters"""
        response = client.get("/sum/this_is_a_string")
        assert response.status_code == 400
        assert response.json() == {"detail": "Invalid input, input has a character " \
                                             "other than a number or comma"}

    def test_double_column(self):
        """test invalid input, when the request has double commas"""
        response = client.get("/sum/23,4,,32")
        assert response.status_code == 400
        assert response.json() == {"detail": "Invalid input, a double column is present " \
                                             "or the input start / ends with a comma"}    

    def test_column_as_first_character(self):
        """test invalid input, when the request starts with a comma"""
        response = client.get("/sum/,4,3,2")
        assert response.status_code == 400
        assert response.json() == {"detail": "Invalid input, a double column is present " \
                                             "or the input start / ends with a comma"}

    def test_column_as_last_character(self):
        """test invalid input, when the request ends in a comma"""
        response = client.get("/sum/4,3,2,")
        assert response.status_code == 400
        assert response.json() == {"detail": "Invalid input, a double column is present " \
                                             "or the input start / ends with a comma"}

    def test_integer_sum(self):
        """test addition of integers"""
        response = client.get("/sum/4,1,3,2")
        assert response.status_code == 200
        assert response.json() == {"sum": 10}

    def test_float_sum(self):
        """test addition when float type is also present"""
        response = client.get("/sum/1,0.2,0.3,0.7,2")
        assert response.status_code == 200
        assert response.json() == {"sum": 4.2}
