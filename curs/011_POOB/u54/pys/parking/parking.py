class Parking:
    def __init__(self, max_spaces):
        self.max_spaces = max_spaces
        self.current_spaces = 0
        self.cars = []

    def check_in(self, car):
        if self.current_spaces < self.max_spaces:
            self.cars.append(car)
            self.current_spaces += 1
            return "Car with license plate {} checked in".format(car)
        else:
            return "Sorry, parking is full"

    def check_out(self, car):
        if car in self.cars:
            self.cars.remove(car)
            self.current_spaces -= 1
            return "Car with license plate {} checked out".format(car)
        else:
            return "Car with license plate {} not found in the parking".format(car)

parking = Parking(5)
print(parking.check_in("ABC123")) # "Car with license plate ABC123 checked in"
print(parking.check_in("DEF456")) # "Car with license plate DEF456 checked in"
print(parking.check_out("ABC123")) # "Car with license plate ABC123 checked out"
print(parking.check_out("GHI789")) # "Car with license plate GHI789 not found in the parking"
