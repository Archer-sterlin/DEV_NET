

def test_user_create(test_client, user_payload):
    response = test_client.post("/blog",json=user_payload)
    assert response.status_code == 200
  