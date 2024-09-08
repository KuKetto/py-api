"""This module tests the query param validation by simulating HTTP requests"""

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

class TestQueryParamValidator:
    """Test query param validator"""
    def test_no_input(self):
        """Test if default factory generates valid input"""
        response = client.get("/validate")
        assert response.status_code == 200

    def test_valid_input(self):
        """Test a valid parameter input"""
        response = client.get("/validate?param=param_valid")
        assert response.status_code == 200
        assert response.json() == {"validation": "success, param_valid is valid"}

    def test_too_short_param(self):
        """Test too short param, param length should be at least 6 characters"""
        response = client.get("/validate?param=param")
        assert response.status_code == 422
        assert response.json()["detail"][0] == {"type": "string_too_short",
                                                "loc": ["query", "param"],
                                                "msg": "String should have at least 6 characters",
                                                "input": "param",
                                                "ctx": {"min_length": 6}}

    def test_too_long_param(self):
        """Test too long param, param length should be at most 70 characters"""
        response = client.get("/validate?param=paramlong540e4cd92151bc159e802241" \
                              "775d0b459459095ed26c551a72036f81eb6a58d5")
        assert response.status_code == 422
        assert response.json()["detail"][0] == {"type": "string_too_long",
                                                "loc": ["query", "param"],
                                                "msg": "String should have at most 70 characters",
                                                "input": "paramlong540e4cd92151bc159e802241775d0b" \
                                                         "459459095ed26c551a72036f81eb6a58d5",
                                                "ctx": {"max_length": 70}}

    def test_invalid_param(self):
        """Test a parameter which does not match the required regex"""
        response = client.get("/validate?param=invalid_param")
        assert response.status_code == 422
        assert response.json()["detail"][0] == {"type": "string_pattern_mismatch",
                                                "loc": ["query", "param"],
                                                "msg": "String should match pattern '^param.*'",
                                                "input": "invalid_param",
                                                "ctx": {"pattern": "^param.*"}}
