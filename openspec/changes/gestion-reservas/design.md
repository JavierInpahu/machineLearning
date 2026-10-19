# Design

## Data Model
- Tabla `reservas` con columnas: id, espacio_id, usuario, fecha, hora.
- Relación: `espacio_id` referencia a tabla `espacios`.

## API Endpoints
- POST /reservas → recibe JSON con espacio_id, usuario, fecha, hora.
- GET /reservas → devuelve lista de reservas.

## Validation
- Antes de insertar, verificar si ya existe reserva para mismo espacio y horario.
