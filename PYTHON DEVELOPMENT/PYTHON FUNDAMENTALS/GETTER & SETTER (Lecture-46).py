class MyClass:
    def __init__(self,value):
        self._value=value

    # Let me explain what is happening in the above code:

    """

    We define a class named 'MyClass'
    Inside the class, We define a constructor (used to mandate the required arguments when creating an object of this class), with an argument 'value'
    Then we define an attribute of the class 'self._value' which holds the value of the parameter 'value' only.
    So, suppose an object 'obj1' is created for the class as below:
    obj1=MyClass(9), Here the value of the argument 'value' is the int '9' 
    then this '9' is also being set as the value of 'Obj1._value',
    So, print(obj1._value) would give us '9'
    
    """

    @property
    def value(self):
        return self._value

    # Let me explain what is happening above in the 2nd part of the code:

    """
    
    Here, We defined a function named 'value' (This has nothing to do with the argument 'value' or attribute '_value' of the class MyClass)
    This function 'value' has 'self' argument,  Which is to specify the object this function can or will be called with.
    when accessed, The function 'value' returns the the _value attribute of that object, which is equal to the argument 'value'
    So, We have the object of the class 'Obj1' defined as: Obj1=MyClass(9)
    Then 'print(Obj1.value)', will print the argument value '9'
    
    """

    # IMPORTANT:

    """
    
    @property is a built-in decorator that allows us to define a method as an attribute of the class rather than a regular method.
    This means that we can define any sort of computation inside the function and call it with the object as an attribute of the class itself,
    Also, the function defined (value) has the same name as the value it returns (_value) for better understanding
    When @property decorator is used, We can access the method like an attribute without needing to use parentheses.
    
    """

    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # SETTER *********************

    """
    We know that we can also set the value of an attribute of the class for a particular object (example 'obj1.age =23')
    But, we can not do the same for getter functions which are acting like a normal attribute
    Rather, we define a decorator 'Setter' for the same, SYNTAX '@Name of the func.setter', See below:
    """

    @property
    def ten_value(self):
        return 10 * self._value

    # The function 'ten_value' returns the 10 times of 'self_value'

    @ten_value.setter
    def ten_value(self,new_value):
        self._value=new_value/10


Obj1=MyClass(21)
print(Obj1.value)

# Now, we can set the value for Obj1.ten_value = whatever we want, and 'self._value' will be 'ten_value/10', See below:

Obj1.ten_value=600

# The value you assign to the attribute (Getter function) is automatically passed as 'new_value' to the setter method.