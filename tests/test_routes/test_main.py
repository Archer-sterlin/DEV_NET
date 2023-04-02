

def test_user_create(test_client, user_payload):
    response = test_client.get("/blog")
    assert response.status_code == 200
  