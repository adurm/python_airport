class Aircraft:

    def __init__(self, cargo_size):
        self.__cargo_size = cargo_size

    def accelerate(self):
        return "Accelerating"

    def breaking(self):
        return "Breaking"

    def get_cargo(self):
        return self.__cargo_size


class FlightTrip:

    def __init__(self, origin, destination, plane_number):
        self.__origin = origin
        self.__destination = destination
        self.__passengers = []
        self.__plane_number = plane_number

    def add_plane(self, number):
        self.__plane_number = number
        return f"Adding plane with number {number}"

    def add_destination(self, destination):
        self.__destination = destination
        return f"Destination {destination} has been added."

    def add_origin(self, origin):
        self.__origin = origin
        return f"Origin {origin} has been added."

    def add_passenger(self, passenger):
        self.__passengers.append(passenger)
        return f"{passenger} has been added to the list of passengers."

    def get_origin(self):
        return self.__origin

    def get_destination(self):
        return self.__destination

    def get_passengers(self):
        return self.__passengers

    def get_plane_number(self):
        return self.__plane_number


class People:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Passenger(People):

    def __init__(self, name, passport_number):
        super().__init__(name)
        self.__passport_number = passport_number

    def get_passport_id(self):
        return self.__passport_number


class Plane(Aircraft):
    def __init__(self, cargo, plane_number):
        super().__init__(cargo)
        self.__plane_number = plane_number

    def get_plane_id(self):
        return self.__plane_number
