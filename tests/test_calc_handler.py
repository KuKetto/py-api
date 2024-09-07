"""This module tests the calc handler by simulating HTTP requests"""

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)
invalid_input = {"detail": "Invalid input. Possible reasons:" \
                           "1) Input has a character other than a " \
                           "number or comma." \
                           "2) Input has multiple commas without a " \
                           "number between them."\
                           "3) Input start with or ends in a comma."}

class TestSum:
    """Test sum handler function"""
    def test_invalid_input(self):
        """test invalid input, when the request has invalid characters"""
        response = client.get("/sum/this_is_a_string")
        assert response.status_code == 400
        assert response.json() == invalid_input

    def test_double_column(self):
        """test invalid input, when the request has double commas"""
        response = client.get("/sum/23,4,,32")
        assert response.status_code == 400
        assert response.json() == invalid_input

    def test_column_as_first_character(self):
        """test invalid input, when the request starts with a comma"""
        response = client.get("/sum/,4,3,2")
        assert response.status_code == 400
        assert response.json() == invalid_input

    def test_column_as_last_character(self):
        """test invalid input, when the request ends in a comma"""
        response = client.get("/sum/4,3,2,")
        assert response.status_code == 400
        assert response.json() == invalid_input

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

class TestLawOfCosine:
    """Test law of cosine handler function"""
    def test_invalid_input(self):
        """test invalid input, when the request has invalid characters"""
        response = client.get("/law_of_cos/side1/test/side2/test")
        assert response.status_code == 400
        assert response.json() == invalid_input

    def test_invalid_geometry_length(self):
        """test invalid input, when the request has invalid geometry length"""
        response = client.get("/law_of_cos/side1/0/side2/42")
        assert response.status_code == 400
        assert response.json() == {"detail": "The given side with length of 0 " \
                                             "is not a valid geometry length."}

    def test_invalid_geometry_angle(self):
        """test invalid input, when the request has invalid geometry angle provided"""
        response = client.get("/law_of_cos/side1/42/side2/42?angle=0")
        assert response.status_code == 400
        assert response.json() == {"detail": "The given angle of 0 " \
                                             "degrees is not a valid geometry angle."}

        response = client.get("/law_of_cos/side1/42/side2/42?angle=720.720")
        assert response.status_code == 400
        assert response.json() == {"detail": "The given angle of 720.720 " \
                                             "degrees is not a valid geometry angle."}

    def test_without_query_param(self):
        """test valid input when the angle query property is not provided"""
        response = client.get("/law_of_cos/side1/3/side2/4")
        assert response.status_code == 200
        assert response.json() == {"side3": 5.0}

    def test_with_query_param(self):
        """test valid input when the angle query property is provided"""
        response = client.get("/law_of_cos/side1/4242.4242/side2/4242.4242?angle=42.42")
        assert response.status_code == 200
        assert response.json() == {"side3": 3069.7102728370523}
