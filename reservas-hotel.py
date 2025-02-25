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
        return f"Nombre: {self.name} {self.surname} Correo: {self.email}"

# Clase Habitacion que representa una habitación en el hotel
class Habitacion:
    def __init__(self, num, type):
        self.num = num
        self.type = type
        self.is_reserved = False  # Por defecto, la habitación está disponible

    def __str__(self):
        state = "Reservada" if self.is_reserved else "Disponible"
        return f"Habitacion numero: {self.num}. Tipo: {self.type}. Estado: {state}"

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
    def reservar_habitacion(self, num):
        if num in self.rooms:
            habitacion = self.rooms[num]
            if habitacion.is_reserved:
                return f"La habitación {num} ya está reservada."
            habitacion.is_reserved = True
            self.reservations.append(habitacion)
            return f"Habitación {num} reservada con éxito."
        else:
            return "La habitación no existe."

    # Cancela una reserva
    def cancelar_reserva(self, num):
        if num in self.rooms:
            habitacion = self.rooms[num]
            if habitacion.is_reserved:
                habitacion.is_reserved = False
                return f"Habitacion {num} cancelada con exito."
            return f"La habitacion {num} esta disponible"
        else:
            return "La habitación no existe."

# Clase Interfaz que maneja la interacción con el usuario
class Interfaz:
    def __init__(self, hotel):
        self.hotel = hotel

    def menu(self):
        while True:
            print("1. Reservar Habitacion")
            print("2. Mostrar Habitaciones")
            print("3. Cancelar Reserva")
            print("4. Salir")
            option = int(input("Introduce una opcion: "))
            if option == 4:
                print("Saliendo...")
                break
            match option:
                case 1:
                    num = int(input("Introduce el número de la habitación que deseas reservar: "))
                    print(self.hotel.reservar_habitacion(num))
                case 2:
                    print(self.hotel.mostrar_habitaciones())
                case 3:
                    num = int(input("Introduce el número de la habitación que deseas cancelar: "))
                    print(self.hotel.cancelar_reserva(num))

# Iniciamos el hotel y el menú
hotel = Hotel("Hotel")
menu = Interfaz(hotel)
menu.menu()
