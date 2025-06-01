class Students():
    """A Simple Model to attempt to MyFarm Students."""

    def __init__(self, 
                 fullname, 
                 major, 
                 age, 
                 duration_time=6
                 ):
        """Initialize the student attributes."""
        self.fullname = fullname
        self.major = major
        self.age = age
        self.duration = duration_time


    def greet_student(self):
        """Print statement to greet the student by there name."""
        print(f"Hello {self.fullname}, Welcome to MyFarm!")

    def student_info(self):
        """Display what you know about the student"""
        std_info = f"\nMy Name is {self.fullname}, am majoring {self.major}, and am {self.age} years old."
        return std_info
    
    def course_duration(self):
        """Display the course duration for ict student"""
        print(f"You have {self.duration} month before graduating.")


class Facilitator(Students):
    """A simple attept to assign facilitator to the student"""
    def __init__(self, fullname, major, age):
        """Initialze an attributes for facilitators"""
        super().__init__(fullname, major, age)
        self.ICT_faci = "Sam"
        self.Bus_faci = "Lamin"
        self.Pro_faci = "Isatou"
    
    def major_dep_faci(self):
        """Display a major department facilitator base on the student department."""
        if self.major == 'ict':
            print(f'Your facilitator is mr.{self.ICT_faci}')

        elif self.major == 'business':
            print(f'Your facilitator is mr.{self.Bus_faci}')

        elif self.major == 'processing':
            print(f'Your facilitator is mr.{self.Pro_faci}')

        else:
            print(f"Error {self.major} myfarm don't have that major or invalid.")


class ICTStudents(Students):
    """get the parent class"""
    def __init__(self, fullname, major, age):
        """Initialize the instace attributes from the superclass"""
        super().__init__(fullname, major, age)


    def upgrade_duration(self):
        """check if student major is ict if so skip."""
        if self.major == 'ict':
            self.duration = 12
            print(f"You are majoring {self.major} your duration has been upgraded.")

        else:
            print(f"You are majoring {self.major} call {self.major} Class instead.")


class Business(Students):
    def __init__(self, fullname, major, age):
        """Initialize business course duration attributes."""
        super().__init__(fullname, major, age)

    def upgrade_duration(self):
        """check if student major is ict if so skip."""
        if self.major == 'business':
            self.duration = 3
            print("The duration has been succefully updated.")
            

        else:
            print(f"You are majoring {self.major} call {self.major} Class instead.")


class Processing(Students):
    def __init__(self, fullname, major, age):
        """Initialize processing course duration attributes."""
        super().__init__(fullname, major, age)


    def upgrade_duration(self):
        """check if student major is ict if so skip."""
        if self.major == 'processing':
           self.duration = 5
           print("The duration has been successfully updated.")

        else:
            print(f"You are majoring {self.major} call {self.major} Class instead.")

    

name = "mama".title()
major = 'business'.lower()
age = 23

mama = Business(name, major, age)
mama.greet_student()
print(mama.student_info())
mama.course_duration()



