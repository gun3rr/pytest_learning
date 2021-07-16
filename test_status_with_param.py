from requests import get
import pytest


@pytest.mark.parametrize("url", ["www.facebook.com", "www.gmail.com"], ids=["FB", "Gmail"])
def test_status(url):
    response = get(url=f"https://{url}")
    assert response.status_code == 200
