## Capabilities

### New Capabilities
- gestion-espacios: Permite registrar y administrar laboratorios, auditorios y salas de cómputo.  
  Cada espacio tiene un identificador único, nombre, capacidad y ubicación.

### Modified Capabilities
- *(ninguno, no hay cambios sobre capacidades existentes)*

## Impact
Este cambio afecta la capa de especificaciones del sistema, creando un nuevo módulo de gestión de espacios académicos.  
Se verán impactados los modelos de datos (espacios), las APIs de registro/consulta y la interfaz de administración.

<success_criteria>
- Registrar un laboratorio con nombre, capacidad y ubicación válidos.
- Intentar registrar un espacio con nombre duplicado debe ser rechazado.
- Consultar la lista de espacios debe mostrar todos los registrados.
</success_criteria>

<unlocks>
Completing this artifact enables: specs, design
</unlocks>
