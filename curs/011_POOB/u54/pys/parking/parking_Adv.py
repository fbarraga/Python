import json

class Parking:
    def __init__(self, spaces, vehicles):
        self.spaces = spaces
        self.vehicles = vehicles

class ParkingLot:
    def __init__(self):
        self.data = {}
        try:
            with open("parking.json", "r") as file:
                self.data = json.load(file)
        except:
            self.data = {"spaces": [], "vehicles": []}
            
    def add_space(self, space_type):
        self.data["spaces"].append(space_type)
        self.save_data()
        
    def add_vehicle(self, vehicle_type):
        self.data["vehicles"].append(vehicle_type)
        self.save_data()

    def save_data(self):
        with open("parking.json", "w") as file:
            json.dump(self.data, file)

def main():
    lot = ParkingLot()
    while True:
        print("1. Add parking space")
        print("2. Add vehicle type")
        print("3. View parking data")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            space_type = input("Enter parking space type: ")
            lot.add_space(space_type)
        elif choice == "2":
            vehicle_type = input("Enter vehicle type: ")
            lot.add_vehicle(vehicle_type)
        elif choice == "3":
            print("Spaces:", lot.data["spaces"])
            print("Vehicles:", lot.data["vehicles"])
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
1