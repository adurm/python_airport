from airport import *

passenger_list = []
plane_list = []
flight_list = []

def switchboard():

    while True:
        print("------------------------------------")
        print("1. Create a new flight")
        print("2. Add passenger")
        print("3. Add Plane")
        print("0. Quit")
        entry = input("> ")

        if entry == '1':
            origin = input("Enter origin of flight: ")
            dest = input("Set destination: ")
            num_of_passengers = input("How many passengers: ")
            plane = input("Enter plane ID: ") - 1
            flight_list.append(FlightTrip(origin, dest, num_of_passengers, plane_list[plane].get_plane_id()))
        elif entry == '2':
            name = input("Enter name: ")
            passenger_list.append(Passenger(name, len(passenger_list) + 1))
        elif entry == '3':
            cargo = int(input("How much cargo can be stored? "))
            plane_list.append(cargo, len(plane_list) + 1)
        elif entry == '0':
            quit()

switchboard()