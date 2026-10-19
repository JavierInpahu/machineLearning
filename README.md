# Sistema de Gestión de Espacios y Reservas

Proyecto desarrollado con FastAPI para la gestión de espacios y reservas, incluyendo validación de duplicados y pruebas automatizadas con pytest.

## Instalación

1. Clona el repositorio o descarga el proyecto.
2. Instala las dependencias necesarias:
   ```bash
   pip install fastapi uvicorn pytest httpx2
Ejecución del servidor
Desde la raíz del proyecto, ejecuta:

bash
python -m uvicorn app:app --reload
El servidor quedará disponible en:

http://127.0.0.1:8000

Documentación interactiva: http://127.0.0.1:8000/docs (127.0.0.1 in Bing)

Endpoints disponibles
Espacios
POST /espacios  
Crear un nuevo espacio.
Ejemplo de entrada:

json
{
  "nombre": "Sala A",
  "capacidad": 30,
  "ubicacion": "Edificio Central"
}
GET /espacios  
Listar todos los espacios registrados.

Reservas
POST /reservas  
Crear una nueva reserva.
Ejemplo de entrada:

json
{
  "espacio": "Sala A",
  "usuario": "Javier",
  "fecha": "2026-10-20",
  "hora": "10:00"
}
GET /reservas  
Listar todas las reservas registradas.

Validaciones implementadas
No se permiten espacios duplicados (mismo nombre).

No se permiten reservas duplicadas en el mismo espacio, fecha y hora.

Pruebas automatizadas
El proyecto incluye pruebas con pytest en la carpeta tests.

Para ejecutarlas:

bash
python -m pytest -v
Cobertura de pruebas
Creación y listado de espacios

Validación de espacios duplicados

Creación y listado de reservas

Validación de reservas duplicadas

Estructura del proyecto
Código
machineLearning/
│
├── app.py                # Aplicación FastAPI
├── README.md             # Documentación del proyecto
├── openspec/             # Artefactos de especificación
│   └── changes/
│       └── gestion-reservas/
│           └── tasks.md
└── tests/                # Pruebas automatizadas
    ├── test_reservas.py
    └── test_espacios.py
Dependencias
fastapi

uvicorn

pytest

httpx2

Autor
Proyecto desarrollado por Javier como parte de la tarea de gestión de espacios y reservas.