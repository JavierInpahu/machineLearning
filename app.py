from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# -------------------------
# Modelo Espacio
# -------------------------
class Espacio(BaseModel):
    nombre: str
    capacidad: int
    ubicacion: str

espacios = []

@app.post("/espacios")
def crear_espacio(espacio: Espacio):
    for e in espacios:
        if e.nombre == espacio.nombre:
            raise HTTPException(status_code=400, detail="El espacio ya existe")
    espacios.append(espacio)
    return {"mensaje": "Espacio creado", "espacio": espacio}

@app.get("/espacios")
def listar_espacios():
    return espacios

# -------------------------
# Modelo Reserva
# -------------------------
class Reserva(BaseModel):
    espacio: str
    usuario: str
    fecha: str
    hora: str

reservas = []

# POST /reservas
@app.post("/reservas")
def crear_reserva(reserva: Reserva):
    # Validar disponibilidad (Task 2.4)
    for r in reservas:
        if r.espacio == reserva.espacio and r.fecha == reserva.fecha and r.hora == reserva.hora:
            raise HTTPException(status_code=400, detail="El espacio ya está reservado en esa fecha y hora")
    reservas.append(reserva)
    return {"mensaje": "Reserva creada", "reserva": reserva}

# GET /reservas
@app.get("/reservas")
def listar_reservas():
    return reservas
