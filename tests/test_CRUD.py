from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_post_orders():
    response = client.post("/api/v1/orders", json={"product": "testing", "quantity": 1, "total_amount": 50.10})
    assert response.status_code == 201
    assert response.json() == {
        "product": "testing",
        "quantity": 1,
        "total_amount": 50.10
    }
    

