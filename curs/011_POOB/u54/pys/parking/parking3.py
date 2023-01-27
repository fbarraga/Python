import json

class Parking:
    def __init__(self, spaces_file):
        self.spaces_file = spaces_file
        self.load_spaces()

    def load_spaces(self):
        try:
            with open(self.spaces_file, "r") as file:
                self.spaces = json.load(file)
        except:
            self.spaces = {"car": [], "motorcycle": [], "bus": []}

    def save_spaces(self):
        with open(self.spaces_file, "w") as file:
            json.dump(self.spaces, file)

    def check_in(self, vehicle_type, license_plate):
        for space_type, spaces in self.spaces.items():
            if vehicle_type == space_type and len(spaces) < len(self.spaces[space_type]):
                spaces.append({"license_plate": license_plate, "status": "occupied"})
                self.save_spaces()
                return f"{vehicle_type} with license plate {license_plate} checked in to space {len(spaces)}"
        return f"No available {vehicle_type} spaces"

    def check_out(self, license_plate):
        for space_type, spaces in self.spaces.items():
            for i, space in enumerate(spaces):
                if space["license_plate"] == license_plate:
                    spaces.pop(i)
                    spaces.append({"license_plate": "", "status": "vacant"})
                    self.save_spaces()
                    return f"{space_type} with license plate {license_plate} checked out"
        return f"No vehicle found with license plate {license_plate}"

    def status(self):
        return self.spaces

if __name__ == "__main__":
    parking = Parking("spaces.json")
    while True:
        print("1. Check In")
        print("2. Check Out")
        print("3. Status")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            vehicle_type = input("Enter vehicle type (car, motorcycle, bus): ")
            license_plate = input("Enter license plate: ")
            print(parking.check_in(vehicle_type, license_plate))
        elif choice == "2":
            license_plate = input("Enter license plate: ")
            print(parking.check_out(license_plate))
        elif choice == "3":
            print(parking.status())
        elif choice == "4":
            break
        else:
            print("Invalid choice")
