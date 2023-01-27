import json

class Parking:
    def __init__(self, name, max_spaces):
        self.name = name
        self.max_spaces = max_spaces
        self.occupied_spaces = 0
        self.parking_data = {"name": self.name, "max_spaces": self.max_spaces, "occupied_spaces": self.occupied_spaces}

    def check_in(self):
        if self.occupied_spaces < self.max_spaces:
            self.occupied_spaces += 1
            self.parking_data["occupied_spaces"] = self.occupied_spaces
            print("Car checked in. Number of occupied spaces:", self.occupied_spaces)
        else:
            print("Parking is full. Please try again later.")

    def check_out(self):
        if self.occupied_spaces > 0:
            self.occupied_spaces -= 1
            self.parking_data["occupied_spaces"] = self.occupied_spaces
            print("Car checked out. Number of occupied spaces:", self.occupied_spaces)
        else:
            print("Parking is empty.")

    def save_to_json(self):
        with open("parking.json", "w") as file:
            json.dump(self.parking_data, file)

# Example usage
parking = Parking("Main Parking", 100)
parking.check_in()
parking.check_in()
parking.check_out()
parking.save_to_json()
