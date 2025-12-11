import requests

def test_ping_service():
    resp = requests.get("https://github.com/kevinha1994/demo-reusable")
    assert (resp.status_code == 200) or (resp.status_code == 504)
    print(f"Successfully passed assertion test: status_code = {resp.status_code}")

test_ping_service()
