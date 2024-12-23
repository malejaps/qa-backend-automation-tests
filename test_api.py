import pytest
import requests
import configuration


@pytest.mark.api_get
def test_get_companies():
    response = requests.get(configuration.URL_SERVICE)
    assert response.status_code == 200, f"Status code not expected: {response.status_code}"






