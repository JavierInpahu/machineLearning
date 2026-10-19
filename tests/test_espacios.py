from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_crear_espacio():
    response = client.post("/espacios", json={
        "nombre": "Aula 101",
        "capacidad": 30,
        "ubicacion": "Edificio A"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["espacio"]["nombre"] == "Aula 101"
    assert data["espacio"]["capacidad"] == 30
    assert data["espacio"]["ubicacion"] == "Edificio A"

def test_listar_espacios():
    response = client.get("/espacios")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(e["nombre"] == "Aula 101" for e in data)

def test_espacio_duplicado():
    response = client.post("/espacios", json={
        "nombre": "Aula 101",
        "capacidad": 40,
        "ubicacion": "Edificio B"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "El espacio ya existe"
