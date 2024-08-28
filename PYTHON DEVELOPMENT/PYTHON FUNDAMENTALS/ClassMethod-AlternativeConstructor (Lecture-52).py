
"""

A class method belongs to the class rather than to an instance of the class.
One common use case for class methods as alternative constructors is when you want to create an object from data that is stored in a different format,
such as a string or a dictionary.

For example, Below is a class named 'Employee' with 2 attributes 'name' & 'salary'
Now, The defined constructor here works if the value for these attributes is passed during object definition something as 'e1 = Employee("Harry", 12000)' simply,
However if we had to create objects for the 'Employee' class where the value for the 2 attributes were to be fetched from strings as "Harry-12000" or "John-14000"
Then instead of slicing the string everytime for each object, We define this action within a method/function under class-method decorator


"""

# Define the Employee Class:
class Employee:
    # Constructor to initialize instance attributes (name and salary):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Create an Instance (e1) using the Constructor:
    e1 = Employee("Harry", 12000)

    # Print Attributes of e1:
    print(e1.name)    # Output: Harry
    print(e1.salary)  # Output: 12000

    # Below contains the code for case 2 where the value for attributes of the object for class 'Employee' are to be fetched from strings

    # Define a Class Method (fromStr) for Alternate Instance Creation:
    @classmethod
    def fromStr(cls, string):                                            # We defined a function 'fromStr' which takes 2 arguments 'cls' and 'string'
        return cls(string.split("-")[0], int(string.split("-")[1]))      # This returns the sliced string for the particular object and updates the 'name' and 'salary' for the class

    # Create an Instance (e2) using the Class Method:
    string = "John-14000"
    e2 = Employee.fromStr(string)

    # Print Attributes of e2:
    print(e2.name)    # Output: John
    print(e2.salary)  # Output: 14000
