class Taxi():
    """A simple taxi model"""

    def __init__(self, driver_name,  location, status='Idle'):
        """Inialize an attributes represent for taxi"""
        self.driver_name = driver_name
        self.location = location
        self.status = status


    def pick_passenger(self, destination):
        """Print statement to show the destination"""
        self.status = 'busy'
        self.destination = destination
        print(f"{self.driver_name.title()} has picked up a passenger heading to {destination}")

    def drop_off(self):
        drop = input("Are you sure you want to drop off here? ['yes'/ 'no'] ")
        if drop == 'yes':
            self.location = self.destination
            self.status = 'Idle'
            print(f"\nPassenger dropped off at {self.location}.")

        elif drop == 'no':
            print("\nOkay! let's keep continue the trip.")

        else:
            print("Invalid input.")
        

    def show_status(self):
        """A method to show the status"""
        print(f"Driver: {self.driver_name.title()}, Location: {self.location.title()}, Status: {self.status.title()}.")


omar_car = Taxi('omar', 'banjul')
omar_car.show_status()
omar_car.pick_passenger('Brikama')
omar_car.drop_off()
