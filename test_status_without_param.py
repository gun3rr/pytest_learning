from requests import get
import pytest


@pytest.mark.positive
@pytest.mark.api
def test_status():
    response = get(url="https://www.facebook.com")
    assert response.status_code == 200


@pytest.mark.negative
@pytest.mark.api
def test_status_negative():
    with pytest.raises(Exception) as e:
        get(url="https://w.face.comfadsfdsafa")
    assert e
