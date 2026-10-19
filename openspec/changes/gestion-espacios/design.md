# Design

## Context

El sistema actualmente no tiene un módulo para gestionar espacios académicos.  
Este diseño define cómo implementar la capacidad de registrar, validar y consultar espacios.  
Ver proposal.md para motivación y alcance.

## Goals / Non-Goals

**Goals:**
- Implementar un modelo de datos para espacios académicos.
- Crear endpoints de API para registrar, consultar y validar espacios.
- Asegurar que no se registren duplicados.
- Integrar validaciones de capacidad y ubicación.

**Non-Goals:**
- No se incluye la gestión de usuarios.
- No se cubre la interfaz gráfica final (solo API y lógica).

## Decisions

- **Modelo de datos:** Tabla `espacios` con campos: id (PK), nombre (único), capacidad (int), ubicación (string).
- **Validación de duplicados:** Constraint único en el campo `nombre`.
- **API:** Endpoint REST `/espacios` con métodos POST (crear), GET (listar).
- **Alternativas consideradas:** Se evaluó usar GraphQL, pero se eligió REST por simplicidad y compatibilidad.

## Risks / Trade-offs

- [Riesgo] → Alta concurrencia podría generar intentos de duplicados.  
  [Mitigación] → Constraint único en BD y manejo de errores en API.  

- [Riesgo] → Escalabilidad limitada si la tabla crece demasiado.  
  [Mitigación] → Posible partición futura o migración a un servicio dedicado.

## Migration Plan

1. Crear tabla `espacios` en la base de datos.  
2. Implementar endpoints REST.  
3. Validar con pruebas unitarias y de integración.  
4. Desplegar en entorno de pruebas → producción.  
5. Rollback: eliminar tabla y deshabilitar endpoints si falla.

## Open Questions

- ¿Se requiere soporte multilingüe para nombres de espacios?  
- ¿La capacidad debe tener un límite máximo configurable?
