from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crear_movimiento():
    response = client.post("/movimientos/", json={
        "tipo": "ingreso",
        "descripcion": "test ingreso",
        "monto": 1500
    })
    assert response.status_code == 200
    assert response.json()["tipo"] == "ingreso"

def test_listar_movimientos():
    response = client.get("/movimientos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
