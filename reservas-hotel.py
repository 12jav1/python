# Clase personalizada para gestionar errores relacionados con las habitaciones
class ErrorRooms(Exception):
    pass

# Clase Cliente que representa a un cliente del hotel
class Cliente:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    def __str__(self):
        return f"🧑 Nombre: {self.name} {self.surname} 📧 Correo: {self.email}"

# Clase Habitacion que representa una habitación en el hotel
class Habitacion:
    def __init__(self, num, type):
        self.num = num
        self.type = type
        self.is_reserved = False  # Por defecto, la habitación está disponible

    def __str__(self):
        status = "❌ Reservada" if self.is_reserved else "✅ Disponible"
        if status == "Reservada":
            return f"🏨 Habitacion numero: {self.num}. 🛏️ Tipo: {self.type}. Estado: {status}"
        else:
            return f"🏨 Habitacion numero: {self.num}. 🛏️ Tipo: {self.type}. Estado: {status}"

# Clase Hotel que maneja las habitaciones y las reservas
class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = {}  # Diccionario para almacenar las habitaciones
        tipos = ["Doble", "Simple", "Suit"]  # Tipos de habitaciones
        tipo_index = 0
        for i in range(100, 121):  # Creamos habitaciones numeradas del 100 al 120
            tipo = tipos[tipo_index]
            self.rooms[i] = Habitacion(i, tipo)  # Añadimos las habitaciones al hotel
            tipo_index = (tipo_index + 1) % len(tipos)
        self.reservations = []  # Lista para almacenar las reservas

    # Muestra todas las habitaciones del hotel
    def mostrar_habitaciones(self):
        habitaciones_info = [str(room) for room in self.rooms.values()]
        return "\n".join(habitaciones_info)

    # Reserva una habitación
    def reservar_habitacion(self, num, customer):
        if num in self.rooms:
            habitacion = self.rooms[num]
            if habitacion.is_reserved:
                return f"⚠️ La habitación {num} ya está reservada."
            habitacion.is_reserved = True
            self.reservations.append((habitacion, customer))
            return f"\n🎉 Habitación {num} reservada con éxito a nombre de {customer.name} {customer.surname} 🏨✨"
        else:
            return "❌ La habitación no existe."

    # Cancela una reserva
    def cancelar_reserva(self, num):
        if num in self.rooms:
            habitacion = self.rooms[num]
            if habitacion.is_reserved:
                habitacion.is_reserved = False
                return f"✅ Habitación {num} cancelada con éxito."
            return f"ℹ️ Esta habitacion no ha sido reservada."
        else:
            return "❌ La habitación no existe."

# Clase Interfaz que maneja la interacción con el usuario
class Interfaz:
    def __init__(self, hotel):
        self.hotel = hotel

    def menu(self):
        while True:
            print("\n🏨 Menú del Hotel:")
            print("1️⃣  Reservar Habitación")
            print("2️⃣  Mostrar Habitaciones")
            print("3️⃣  Cancelar Reserva")
            print("4️⃣  Salir\n")

            try:
                option = int(input("👉 Introduce una opción: "))
            except ValueError:
                print("⚠️ Error: Debes introducir un número válido. Intenta de nuevo.")
                continue

            if option == 4:
                print("👋 Saliendo...")
                break
            
            match option:
                case 1:
                    name_customer = input("📝 Introduce tu nombre: ").capitalize()
                    surname_customer = input("📝 Introduce tu apellido: ").capitalize()
                    email_customer = input("📧 Introduce tu email: ").lower()
                    customer = Cliente(name_customer, surname_customer, email_customer)

                    while True:
                        try:
                            num = int(input("🔢 Introduce el número de la habitación que deseas reservar: "))
                            break
                        except ValueError:
                            print("⚠️ Error: Introduce un número válido para la habitación.")

                    print(self.hotel.reservar_habitacion(num, customer))

                case 2:
                    print("\n📋 Estado actual de las habitaciones:")
                    print(self.hotel.mostrar_habitaciones())

                case 3:
                    while True:
                        try:
                            num = int(input("🔢 Introduce el número de la habitación que deseas cancelar: "))
                            break
                        except ValueError:
                            print("⚠️ Error: Introduce un número válido para la habitación.")

                    print(self.hotel.cancelar_reserva(num))

                case _:
                    print("⚠️ Opción no válida. Intenta de nuevo.")

# Iniciamos el hotel y el menú
hotel = Hotel("Hotel")
menu = Interfaz(hotel)
menu.menu()