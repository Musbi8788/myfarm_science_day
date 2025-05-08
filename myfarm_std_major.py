class Myfarm_student:
    """A Simple program that will take student name with their mejor department and show it to them"""


    def __init__(self, std_name, major_dpt):
        self.std_name = std_name
        self.major_dpt = major_dpt

    def describe_mf_std(self):
        print(f"\nMy name is {self.std_name}.")
        print(f"I'm majoring {self.major_dpt} department.\n")

    def science_day(self):
        print(f"{self.std_name} tommorow is science day.\n")


# add many instance as you can.
hawa = Myfarm_student('Hawa', 'ICT')
hawa.describe_mf_std()
hawa.science_day()