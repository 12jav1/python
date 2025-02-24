class ErrorRooms(Exception):
    pass

class Cliente:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    def __str__(self):
        return f"Nombre: {self.name} {self.surname} Correo: {self.email}"

    
class Habitacion:
    def __init__(self, num, type):

        if num < 100 or num > 110:
            raise ErrorRooms ("El numero de habitaciones tiene que estar entre 100 y 110")

        self.num = num
        self.type = type
        self.is_reserved = False # True si está reservada, False si está disponible

    def reserve(self):
        self.estado = True

    def free(self):
        self.estado = False

    def __str__(self):
        return f"Habitacion numero: {self.num}. Tipo: {self.type} Estado: {self.estado}"
    

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.reservations = []

    def add_rooms(self, room):
        self.rooms.append(room)
        
    def make_reservation(self, customer, room_number):
        pass
