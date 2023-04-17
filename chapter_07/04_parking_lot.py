from abc import abstractmethod
from enum import IntEnum
from random import randrange


class VehicleSize(IntEnum):
    Motorcycle = 0
    Compact = 1
    Large = 2

class Vehicle():
    def __init__(self, spot_needed, vehicle_size, license_plate = None):
        self.parking_spot = list()
        self.license_plate = license_plate
        self.spot_needed = spot_needed
        self.vehicle_size = vehicle_size

    def get_spot_needed(self):
        return self.spot_needed

    def get_vehicle_size(self):
        return self.vehicle_size

    def park_in_spot(self, parking_in_spot):
        self.parking_spot.append(parking_in_spot)

    def clear_spot(self):
        for i in range(len(self.parking_spot)):
            self.parking_spot[i].remove_vehicle()
        self.parking_spot.clear()

    @abstractmethod
    def can_fit_in_spot(self, spot):
        pass

class Bus(Vehicle):
    def __init__(self):
        super().__init__(5, VehicleSize.Large)

    def can_fit_in_spot(self, spot):
        return spot.get_size() == VehicleSize.Large.value

class Car(Vehicle):
    def __init__(self):
        super().__init__(1, VehicleSize.Compact)

    def can_fit_in_spot(self, spot):
        return spot.get_size() == VehicleSize.Compact.value or \
                spot.get_size() == VehicleSize.Large.value

class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__(1, VehicleSize.Motorcycle)

    def can_fit_in_spot(self, spot):
        return True

class ParkingLot:
    NUM_LEVEL = 3
    NUM_SPOTS = 10

    def __init__(self):
        self.levels = [Level(i, self.NUM_SPOTS) for i in range(self.NUM_LEVEL)]

    def park_vehicle(self, vehicle):
        for i in range(len(self.levels)):
            return self.levels[i].park_vehicle(vehicle)
        return False

class Level:
    def __init__(self, floor, number_spots):
        self.floor = floor
        self.spots = []
        self.available_spots = number_spots
        self.spots_per_row = 10

        for i in range(number_spots):
            spot_size = VehicleSize.Motorcycle.value
            if i < number_spots:
                spot_size = VehicleSize.Large.value
            elif i < (number_spots * 2):
                spot_size = VehicleSize.Compact.value
            self.spots.append(ParkingSpot(self, i//self.spots_per_row, i, spot_size))

    def get_available_spots(self):
        return self.available_spots

    def spot_freed(self):
        self.available_spots += 1

    def park_vehicle(self, vehicle):
        if self.get_available_spots() < vehicle.get_spot_needed():
            return False
        spot_number = self.find_available_spots(vehicle)
        return False if spot_number < 0 else self.park_starting_at_spot(spot_number, vehicle)

    def park_starting_at_spot(self, spot_number, vehicle):
        vehicle.clear_spot()
        is_success = True
        for i in range(spot_number, spot_number+vehicle.get_spot_needed()):
            is_success = is_success & self.spots[i].park(vehicle)
        self.available_spots -= vehicle.get_spot_needed()
        return is_success

    def find_available_spots(self, vehicle):
        last_row = -1
        spots_found = 0
        for i in range(len(self.spots)):
            spot = self.spots[i]
            if last_row != spot.get_row():
                spots_found = 0
                last_row = spot.get_row()
            if spot.can_fit_vehicle(vehicle):
                spots_found += 1
            else:
                spots_found = 0
            if spots_found == vehicle.get_spot_needed():
                return i - (vehicle.get_spot_needed()-1)
        return -1

class ParkingSpot:
    def __init__(self, level, row, number, spot_size, vehicle=None):
        self.vehicle = vehicle
        self.spot_size = spot_size
        self.row = row
        self.level = level
        self.spot_number = number

    def is_available(self):
        return self.vehicle == None

    def can_fit_vehicle(self, vehicle):
        return self.is_available() and vehicle.can_fit_in_spot(self)

    def park(self, vehicle):
        if not self.can_fit_vehicle(vehicle):
            return False
        self.vehicle = vehicle
        self.vehicle.park_in_spot(self)
        return True

    def get_row(self):
        return self.row

    def get_spot_number(self):
        return self.spot_number

    def remove_vehicle(self):
        self.level.spot_freed()
        self.vehicle = None

    def get_size(self):
        return self.spot_size


if __name__ == "__main__":
    parking_lot = ParkingLot()
    vehicle = Motorcycle()
    while parking_lot.park_vehicle(vehicle):
        random_num = randrange(0, 10)
        if random_num < 4:
            vehicle = Motorcycle()
        elif random_num < 7:
            vehicle = Car()
        else:
            vehicle = Bus()
        print("parked vehicle")
    print("full of parking lot")
