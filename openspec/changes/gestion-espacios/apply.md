# Apply

## Migration Plan
- [ ] 1.1 Migraciones de base de datos  
  Crear la tabla `espacios` con campos: id (PK), nombre (único), capacidad y ubicación  

- [ ] 1.2 Implementación de endpoints  
  - POST `/espacios`: recibe datos válidos y registra un nuevo espacio  
  - GET `/espacios`: devuelve la lista completa de espacios registrados  

- [ ] 1.3 Validaciones de duplicados  
  - Constraint único en el campo `nombre`  
  - Manejo de error en API: devolver mensaje claro si se intenta registrar un duplicado  

- [ ] 1.4 Pruebas unitarias e integración  
  - Unit tests para validaciones de modelo y API  
  - Integration tests para flujo completo: registro, consulta y rechazo de duplicados  

- [ ] 1.5 Estrategia de despliegue y rollback  
  - Desplegar primero en entorno de pruebas  
  - Validar con casos de prueba automatizados  
  - Rollback: eliminar tabla `espacios` y deshabilitar endpoints si falla la implementación  

## Success Criteria
- Todos los escenarios de `spec.md` se cumplen en pruebas automatizadas.  
- Los endpoints responden correctamente en entorno de pruebas.  
- La base de datos mantiene integridad y evita duplicados.  
