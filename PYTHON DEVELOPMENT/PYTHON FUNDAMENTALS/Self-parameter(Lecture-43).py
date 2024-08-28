# self parameter:

"""
The 'self' parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
"""

# IMPORTANT: It must be provided as the extra parameter inside the method definition.

# Example:

class Details:
    name = "Rohan"
    age = 20

    """
    
    Suppose, we define a function named 'desc' inside the class itself which prints an f-string,
    and we also have an object say 'a' & 'b' which hold different values for attribute name and age,
    To customize this f-string with the values of an object's attributes, such as 'name' and 'age,' we pass 'self' as an argument
    and then call the function using the object itself. This way, the function will use the specific attribute values of the object it's called with.
    
    """

    def desc(self):                                                             # We defined the func 'desc' with 'self' as argument
        print(f"My name is", self.name, "and I'm", self.age, "years old.")      # Prints the f-string

a = Details()
a.name='Ratnesh'
a.age = 24

a.desc()               # Calling the function with 'a', updates attribute values

b = Details()
b.name = 'Neha'
b.age = 23

b.desc()              # Calling the function with 'a', updates attribute values
