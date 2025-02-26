# Sistema de Gestión de Reservas de Hotel

Este repositorio contiene un sistema de gestión de reservas para hoteles desarrollado en Python. El sistema permite administrar habitaciones, realizar reservas, visualizar el estado de las habitaciones y cancelar reservas existentes.

## Características

- 🏨 Gestión completa de habitaciones de hotel con diferentes tipos (Doble, Simple, Suit)
- 📝 Registro de clientes con validación de correo electrónico
- ✅ Sistema de reservas con validación de disponibilidad
- ❌ Cancelación de reservas
- 📊 Visualización del estado actual de todas las habitaciones

## Estructura

El script `reservas-hotel.py` está organizado en cuatro clases principales:

### Customer (Cliente)
Gestiona la información de los clientes que realizan reservas:
- Nombre y apellido
- Correo electrónico

### Room (Habitación)
Representa cada habitación del hotel:
- Número de habitación
- Tipo de habitación (Simple, Doble, Suit)
- Estado de la reserva (disponible o reservada)

### Hotel
Administra el conjunto de habitaciones y las reservas:
- Creación automática de habitaciones (numeradas del 100 al 110)
- Visualización del estado de todas las habitaciones
- Realización de reservas
- Cancelación de reservas

### Interface (Interfaz)
Maneja la interacción con el usuario mediante un menú interactivo:
- Reserva de habitaciones
- Visualización de habitaciones
- Cancelación de reservas

## Uso

1. Ejecuta el script desde la terminal:
   ```
   python reservas-hotel.py
   ```

2. Utiliza el menú interactivo para:
   - Reservar una habitación (opción 1️⃣)
   - Ver el estado de todas las habitaciones (opción 2️⃣)
   - Cancelar una reserva existente (opción 3️⃣)
   - Salir del programa (opción 4️⃣)

## Ejemplo de uso

### Reserva de habitación
```
🏨 Menú del Hotel:
1️⃣  Reservar Habitación
2️⃣  Mostrar Habitaciones
3️⃣  Cancelar Reserva
4️⃣  Salir

👉 Introduce una opción: 1
📝 Introduce tu nombre: Juan
📝 Introduce tu apellido: Pérez
📧 Introduce tu email: juan.perez@email.com
🔢 Introduce el número de la habitación que deseas reservar: 103

🎉 Habitación 103 reservada con éxito a nombre de Juan Pérez
```

### Visualización de habitaciones
```
🏨 Menú del Hotel:
1️⃣  Reservar Habitación
2️⃣  Mostrar Habitaciones
3️⃣  Cancelar Reserva
4️⃣  Salir

👉 Introduce una opción: 2

📋 Estado actual de las habitaciones:
🏨 Habitacion numero: 100. 🛏️  Tipo: Doble. Estado: ✅ Disponible
🏨 Habitacion numero: 101. 🛏️  Tipo: Simple. Estado: ✅ Disponible
🏨 Habitacion numero: 102. 🛏️  Tipo: Suit. Estado: ✅ Disponible
🏨 Habitacion numero: 103. 🛏️  Tipo: Doble. Estado: ❌ Reservada
...
```

### Cancelación de reserva
```
🏨 Menú del Hotel:
1️⃣  Reservar Habitación
2️⃣  Mostrar Habitaciones
3️⃣  Cancelar Reserva
4️⃣  Salir

👉 Introduce una opción: 3
🔢 Introduce el número de la habitación que deseas cancelar: 103
✅ Habitación 103 cancelada con éxito.
```

## Requisitos

- Python 3.10 o superior (se utiliza la sintaxis `match/case`)

## Características Técnicas

- Implementación orientada a objetos con 4 clases bien definidas
- Validación de datos de entrada
- Manejo de errores para entradas incorrectas
- Interfaz de consola con emojis para mejorar la experiencia de usuario
- Control de estado para evitar reservas duplicadas

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este sistema, puedes:

1. Hacer un fork del repositorio
2. Crear una rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`)
3. Hacer commit de tus cambios (`git commit -am 'Añadir nueva funcionalidad'`)
4. Hacer push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear un Pull Request

## Posibles Mejoras

- Persistencia de datos (guardar reservas en un archivo o base de datos)
- Interfaz gráfica utilizando bibliotecas como Tkinter o PyQt
- Sistema de fechas para reservas por periodos
- Funcionalidades adicionales como facturación o servicios adicionales

## Licencia

Este proyecto está licenciado bajo [MIT License](LICENSE).
