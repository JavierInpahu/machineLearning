# Spec Delta

## Purpose
Permite a los usuarios registrar y consultar reservas de espacios académicos, asegurando disponibilidad y evitando conflictos de uso.

## ADDED Requirements

### Requirement: Crear tabla reservas
El sistema SHALL crear la tabla `reservas` con id único, espacio_id, usuario, fecha y hora.

#### Scenario: Creación de tabla
- **WHEN** se despliega la base de datos
- **THEN** se crea la tabla `reservas` con las columnas definidas

### Requirement: Registrar reserva
El sistema SHALL permitir registrar una reserva asociada a un espacio y usuario en una fecha y hora específicas.

#### Scenario: Registro exitoso
- **WHEN** el usuario envía datos válidos
- **THEN** el sistema guarda la reserva y devuelve confirmación

### Requirement: Listar reservas
El sistema SHALL permitir consultar todas las reservas registradas.

#### Scenario: Consulta exitosa
- **WHEN** el usuario solicita la lista de reservas
- **THEN** el sistema devuelve todas las reservas existentes

### Requirement: Validar disponibilidad
El sistema SHALL rechazar reservas que intenten ocupar un espacio ya reservado en la misma fecha y hora.

#### Scenario: Reserva duplicada
- **WHEN** se intenta reservar un espacio ocupado
- **THEN** el sistema devuelve error indicando que el espacio no está disponible
