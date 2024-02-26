# class creation
class Student:
    def __init__(self, name, mat_number):
        # creating an attribute
        self.name= name;
        self.mat_number = mat_number

    def display_info(self):
        print(f"Name: {self.name}\n mat number : {self.mat_number}")
# creating an object
student1 = Student("JAMES ", "FUO")
student1.display_info()