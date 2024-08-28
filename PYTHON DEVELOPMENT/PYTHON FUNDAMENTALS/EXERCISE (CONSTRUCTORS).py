"""
Exercise: Student Information

Create a Python class called Student to represent student information. The class should have the following attributes and methods:

Attributes:

name: A string representing the student's name.
age: An integer representing the student's age.
roll_number: A string representing the student's roll number.
marks: A dictionary where the keys are subject names (e.g., "Math", "Science") and the values are the student's marks in those subjects.
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
__init__(self, name, age, roll_number): The constructor should initialize the name, age, and roll number. The marks dictionary should be empty initially.

add_mark(self, subject, mark): A method to add a mark for a subject.
The subject is a string representing the subject name, and mark is the integer representing the student's score in that subject.

get_average(self): A method that calculates and returns the average marks of the student.

display_info(self): A method that prints the student's information and their marks in a user-friendly way.

Create an instance of the Student class, add marks for different subjects, and calculate and display the average marks and student information.
"""

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class Student():
    def __init__(self,name,age,roll_number,marks):
        self.name = name
        self.age = age
        self.roll_number = roll_number
        self.marks = marks

    def add_mark(self,subject,mark):
        self.marks.update({subject: mark})


    def get_average(self):
        values=list(self.marks.values())
        print(f"Average marks for {self.name} are {sum(values)/len(values)}")

    def display_info(self):
        print(f"{self.name} is a {self.age} year old student with roll number {self.roll_number}")

        for subject, mark in self.marks.items():
            print(f"{subject} = {mark}")

Obj1 = Student("Ratnesh",22,18,{'Science':33,'Maths':45,'English':65})

Obj1.get_average()
Obj1.add_mark('Evs',31)
Obj1.display_info()

print()

Obj2 = Student("Vidyut",23,19,{'Science':39,'Maths':76,'English':46})

Obj2.get_average()
Obj2.add_mark('Evs',61)
Obj2.display_info()