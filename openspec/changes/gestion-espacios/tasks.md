- [x] 1.1 Crear tabla espacios  
  **WHEN** se despliega la base de datos  
  **THEN** se crea la tabla `espacios` con id, nombre único, capacidad y ubicación  

- [x] 1.2 Implementar endpoint POST /espacios  
  **WHEN** el usuario envía datos válidos  
  **THEN** el sistema guarda el espacio y devuelve confirmación  

- [x] 1.3 Implementar endpoint GET /espacios  
  **WHEN** el usuario solicita la lista  
  **THEN** el sistema devuelve todos los espacios registrados  

- [x] 1.4 Validar duplicados  
  **WHEN** se intenta registrar un espacio con nombre existente  
  **THEN** el sistema rechaza y muestra error
