from apps.app import app

def test_home():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert res.get_json()["message"] == "Hello, Ebryx CI/CD!"
