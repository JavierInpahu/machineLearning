# Spec Delta

## Purpose
Permite registrar y administrar espacios académicos (laboratorios, auditorios y salas de cómputo) con datos únicos y validados.

## ADDED Requirements

### Requirement: Registrar espacio académico
El sistema SHALL permitir registrar laboratorios, auditorios y salas de cómputo con identificador único, nombre, capacidad y ubicación.

#### Scenario: Registro exitoso
- **WHEN** el usuario ingresa nombre, capacidad y ubicación válidos
- **THEN** el sistema guarda el espacio y lo muestra en la lista

### Requirement: Validar duplicados
El sistema SHALL rechazar espacios con nombre duplicado.

#### Scenario: Registro duplicado
- **WHEN** el usuario intenta registrar un espacio con nombre ya existente
- **THEN** el sistema rechaza el registro y muestra un mensaje de error

### Requirement: Consultar espacios
El sistema SHALL permitir consultar la lista de espacios registrados.

#### Scenario: Consulta exitosa
- **WHEN** el usuario solicita la lista de espacios
- **THEN** el sistema muestra todos los espacios registrados

## REMOVED Requirements
*(ninguno)*

<success_criteria>
Todos los escenarios definidos deben poder probarse como casos de prueba.
</success_criteria>