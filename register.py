class User:
    """A simple attempt to represent a user"""

    def __init__(self, name ,age, role='back'):
        """Initialize name , age and roll attributes."""
        self.name = name 
        self.age = age 
        self.role = role

    def display_info(self):
        """Print statement to display user info"""
        print(f"My name is {self.name.title()} am {self.age} years old and my role is {self.role}.")

    def is_adult(self):
        """Check if user is adult or not"""
        if self.age >= 18:
            print(f"{self.name} you are an adult.\n")

        else:
            print(f"{self.name} you are still young.\n")




fatou = User('fatou', 20)
fatou.display_info()
fatou.is_adult()

lamin = User('lamin', 30)
lamin.display_info()
lamin.is_adult()

omar = User('omar', 10)
omar.display_info()
omar.is_adult()