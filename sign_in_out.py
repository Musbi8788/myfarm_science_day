from datetime import date
import time

class MyFarmUser():
    """A real world sign in/out board."""
    users = ['sam', 'jim', 'isatou', 'musbi', 'lamin']

    def __init__(self, name, role, status_in_out):
        """Initialze name, roll, status attributes."""
        self.name = name
        self.role = role
        self.status = status_in_out
        self.sign_date = date.today()
    
    def display_info(self):
        """display user information"""
        info_in = f"Name: {self.name.title()}\nPosition: {self.role.title()}\nStatus: Sign {self.status.title()}\nTime: {self.time_sign}\nDate: {self.sign_date}\n"
        print(info_in)

    def sign_in(self):
        """Simulate person sign in"""
        self.time_sign = time.strftime("%H:%M:%S %p")
        self.status = 'in'
        self.display_info()


    def sign_out(self):
        """Simulate person sign out"""
        self.time_sign = time.strftime("%H:%M:%S %p")
        self.status = 'out'
        self.display_info()
        

    def get_status(self):
        """get the person status"""
        if self.name.lower() in MyFarmUser.users:

            # check if the user is signing in.
            if self.status.lower() == 'in':
                self.sign_in()

            # check if the user is signing out.
            elif self.status.lower() == 'out':
                self.sign_out()

            else:
                # user not in the list.
                print(f"Unknown |{self.status}| for {self.name.title()}.\n")

        else:
            print(f"Invalid name {self.name.title()} not in list.\n")

# Results
users = [
        MyFarmUser('sam', 'head of ict', 'out') ,
        MyFarmUser('jim', 'manager', 'in'),
        MyFarmUser('omar', 'student', 'out'),
        MyFarmUser('lamin', 'facilitator', 'out'),
        MyFarmUser('awa', 'student', 'out'),
        MyFarmUser('musbi', 'python dev', 'coding'),
        ]

for user in users:
    user.get_status()


