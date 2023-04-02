import pytest
from fastapi.testclient import TestClient


from main import app

client = TestClient(app)


@pytest.fixture(scope="module")
def test_client() -> TestClient:
    """
    create test client instance
    """
    client = TestClient(app)
    yield client  


@pytest.fixture(scope="module")
def blog_payload() -> dict:
    """
    create test client instance
    """
    payload = {
        "title": "blog title",
        "body": "blog body",
         }
    
    return payload 


@pytest.fixture(scope="module")
def user_payload() -> dict:
    payload: dict = {
            "name": "killer bean",
            "email": "killerbeanforever@gmail.com",
            "is_active": True,
            "is_superuser": False,
            "password": "killerbeanforever" 
    }

    return payload 

