import json
from fastapi.testclient import TestClient

from app.main import app
from app.models.company import Company

client = TestClient(app)


def test_create_user():
    company = {
        "name": "NashTech Gglobal",
        "description": "NashTech Gglobal",
        "mode": 1,
        "rating": 1
    }
    response = client.post("/users", json=json.dumps(company))
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Tien Nguyen :D"}
