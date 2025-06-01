class Person():
    """A basic person"""

    def __init__(self, name, gender):
        """Initialize name and gender attributes"""
        self.name = name
        self.gender = gender
    def introduce(self):
        print(f"My Name is {self.name.title()} and am a {self.gender.title()}")

class Student(Person):
    """Student class"""

    def __init__(self, name , gender, department):
        """Initialize a parent class"""
        super().__init__(name, gender,)
        self.department = department

    def show_info(self):
        """A print statement to show the student information."""
        full_details = f"Name: {self.name.title()},\nGender: {self.gender.title()},\nDepartment: {self.department.title()}."

        print(full_details)

    def introduce(self):
        """override introduce method"""
        print(f"Hello, I'm {self.name.title()}, am a student in the {self.department.title()} department.\n")



class Staff(Person):
    """Staff class"""

    def __init__(self, name , gender, position):
        """Initialize a parent class"""
        super().__init__(name, gender,)
        self.position = position

    def show_info(self):
        """A print statement to show the student information."""
        full_details = f"Name: {self.name.title()},\nGender {self.gender.title()},\nPosition: {self.position.title()}."
        
        print(full_details)

    def introduce(self):
        """override introduce method"""
        print(f"Hello, I'm {self.name.title()}, am a staff my position is {self.position.title()}.\n")

musbi = Student('musbi', 'man', 'ict')
musbi.show_info()
musbi.introduce()


sam = Staff('sam', 'man', 'head of ict department')
sam.show_info()
sam.introduce()