import pytest
import requests
import configuration
from jsonschema import validate

@pytest.mark.api_get
def test_get_companies():
    response = requests.get(configuration.URL_SERVICE)
    assert response.status_code == 200, f"Status code not expected: {response.status_code}"

@pytest.mark.api_schema
def test_expected_schema():
    expected_schema = {
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "address": {"type": "string"},
            "zip": {"type": "string"},
            "country": {"type": "string"},
            "employeeCount": {"type": "integer"},
            "industry": {"type": "string"},
            "marketCap": {"type": "integer"},
            "domain": {"type": "string"},
            "logo": {"type": "string"},
            "ceoName": {"type": "string"},
        },
        "required": ["id", "name", "address", "zip", "country", "employeeCount", "industry", "marketCap", "domain", "logo", "ceoName"],
    }
    response = requests.get(configuration.URL_SERVICE)
    json_data = response.json()
    try:
        validate(instance=json_data, schema=expected_schema)
    except Exception as e:
        assert False, f"JSON doesn't have the expected schema {e}"