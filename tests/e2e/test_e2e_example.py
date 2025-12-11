import requests

def test_ping_service():
    resp = requests.get("https://github.com/kevinha1994/demo-reusable")
    assert resp.status_code == 200
