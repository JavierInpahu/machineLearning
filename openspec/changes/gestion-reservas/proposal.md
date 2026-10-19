# Proposal

## Why
Los espacios ya se pueden registrar y consultar, pero falta permitir que los usuarios reserven un espacio en una fecha y hora específicas.  
Este cambio asegura control de disponibilidad y evita conflictos de uso.

## What Changes
Se introduce la gestión de reservas: creación, consulta y validación de disponibilidad de espacios.

## Capabilities

### New Capabilities
- gestion-reservas: Permite registrar y administrar reservas de espacios académicos.  
  Cada reserva tiene un identificador único, referencia al espacio, usuario solicitante, fecha y hora.

### Modified Capabilities
- *(ninguno, no hay cambios sobre capacidades existentes)*

## Impact
Este cambio afecta:
- Modelos de datos (tabla reservas con relación a espacios).  
- Endpoints de la API (`POST /reservas`, `GET /reservas`).  
- Lógica de validación para evitar reservas duplicadas en el mismo espacio y horario.
