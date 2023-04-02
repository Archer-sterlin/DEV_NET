

def test_blog_create(test_client, blog_payload):
    response = test_client.post("/blog",json=blog_payload)
    assert response.status_code == 200

def test_user_create(test_client, user_payload):
    response = test_client.post("/user",json=user_payload)
    assert response.status_code == 200