"""

Student Class:
Write a Student class with attributes such as name, age, and marks.
Implement methods to add marks for different subjects, calculate the average, and display student details.

"""

class Student:                                          # We created a class 'Student'
    def __init__(self,name,age):                        # We created a constructor (Whenever we would create an object for this class, We need to give the name and age of the object)
        self.name=str(name)                             # We created the instance variable 'self.name' and assigned it to string type variable 'name'
        self.age=int(age)                               # We created the instance variable 'self.age' and assigned it to int type variable 'age'
        self.marks=[]                                   # We created the instance variable 'self.marks' and assigned it an empty list to store marks later on

        # NOTE: We did not define any argument variable for self.marks inside the constructor as we do not require marks to be initiated while creating the object, rather during the function call you will see below

    def average(self):                                  # We define a function that would calculate the average of marks
        print(f"The average for the marks is "          # We print an f-string that calculates the average 
              f"{sum(self.marks)/len(self.marks)}")

    def add_marks(self,new_marks):                      # We define a function to add marks to our pre-defined empty list for 'self.marks' instance variable (line-13)
        self.marks.append(new_marks)                    # We append the value for 'new_marks' argument to the list 'self.marks'

    def display(self):                                                  # We define a function to display the details of the object of class 'Student'
        for i,value in enumerate(self.marks, start=1):                  # We use enumerate function to iterate over the list 'self.marks' where 'i' holds the index and 'value' holds the value at that index of the list
            print(f"{self.name} has scored {value} in subject {i}")     # We print an f-string


obj1=Student("Ratnesh",21)
obj1.add_marks(34)
obj1.add_marks(64)
obj1.add_marks(82)
obj1.display()
obj1.average()