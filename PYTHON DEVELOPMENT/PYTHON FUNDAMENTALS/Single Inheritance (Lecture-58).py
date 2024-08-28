"""

Single inheritance is a type of inheritance where a class inherits properties and behaviors from a single parent class.
This is the simplest and most common form of inheritance.
SYNTAX:
class ChildClass(ParentClass):
    # class body

"""

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark!")


d = Dog("Coco", "Doberman")
d.make_sound()

a = Animal("Coco", "Dog")
a.make_sound()


# Quick Quiz: Implement a Cat class by using the animal class. Add some methods specific to cat


class cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print(f"Meaow!")

c= cat("Gold", "Swift")
c.make_sound()


