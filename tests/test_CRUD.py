import sys
import os

# Adicione o diretório raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_post_orders():
    response = client.post("/api/v1/orders", json={"product": "testing", "quantity": 1, "total_amount": 50.10})
    assert response.status_code == 203
    assert response.json() == {
        "product": "testing",
        "quantity": 1,
        "total_amount": 50.10
    }
    

