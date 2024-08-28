"""

Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method in a derived class.
The method in the derived class is said to override the method in the base class.
When you create an instance of the derived class and call the overridden method,
the version of the method in the derived class is executed, rather than the version in the base class.

"""

class Employee:
    def __init__(self, id, salary, age):
        self.id = id
        self.salary = salary
        self.age = age

    def show(self):
        return f"The employee with id {self.id} is earning {self.salary} at the age of {self.age}"

first = Employee(1,56000,23)

print(first.show())

class Programmer(Employee):
    def __init__(self, id, salary, age, lang):
        self.lang = lang
        super().__init__(id, salary, age)

    def show(self):
        return f"The Programmer with id {self.id} is earning {self.salary} at the age of {self.age} coding in {self.lang}"

second = Programmer(2,78000,43, "python")
print(second.show())


"""

Method overriding occurs when a subclass provides a specific implementation for a method that is already defined in its superclass.
In the Programmer class, the show method is overridden to provide a specific implementation for programmers.
The overridden method includes additional information about the programming language (self.lang).
When you call second.show(), it invokes the overridden method in the Programmer class rather than the method in the Employee class.

"""

