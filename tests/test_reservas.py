from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_crear_espacio():
    response = client.post("/espacios", json={
        "nombre": "Sala A",
        "capacidad": 30,
        "ubicacion": "Edificio Central"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["espacio"]["nombre"] == "Sala A"

def test_crear_reserva():
    response = client.post("/reservas", json={
        "espacio": "Sala A",
        "usuario": "Javier",
        "fecha": "2026-10-20",
        "hora": "10:00"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["reserva"]["usuario"] == "Javier"

def test_reserva_duplicada():
    response = client.post("/reservas", json={
        "espacio": "Sala A",
        "usuario": "Javier",
        "fecha": "2026-10-20",
        "hora": "10:00"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "El espacio ya está reservado en esa fecha y hora"

def test_listar_reservas():
    response = client.get("/reservas")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(r["usuario"] == "Javier" for r in data)
