# Tasks

- [x] 2.1 Crear tabla reservas  
  **WHEN** se despliega la base de datos  
  **THEN** se crea la tabla `reservas` con id, espacio_id, usuario, fecha y hora  

- [x] 2.2 Implementar endpoint POST /reservas  
  **WHEN** el usuario envía datos válidos  
  **THEN** el sistema guarda la reserva y devuelve confirmación  

- [x] 2.3 Implementar endpoint GET /reservas  
  **WHEN** el usuario solicita la lista de reservas  
  **THEN** el sistema devuelve todas las reservas registradas  

- [x] 2.4 Validar disponibilidad de espacios  
  **WHEN** se intenta reservar un espacio ocupado  
  **THEN** el sistema rechaza y muestra error
