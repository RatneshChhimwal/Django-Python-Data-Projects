# TYPECASTING

a="1"
b="2"

print(a+b) # This will rather print '12' instead of '3' as the value stored in variable 'a' and 'b' are string type

# If we still want to perform the addition while keeping 'a' & 'b' as integers, we will have to convert the values to integer or float type during the definition of function

print(int(a)+int(b))


# TYPES OF TYPECASTING:

'''

Explicit Typecasting (Type Casting): ----------

Explicit typecasting is the manual conversion of one data type to another by using built-in functions or constructors explicitly.
It requires the programmer to specify the desired target data type.

Implicit Typecasting (Type Coercion): ---------

Implicit typecasting is the automatic conversion of one data type to another by the Python interpreter.
It occurs when Python automatically converts one data type to another in expressions or operations, based on certain rules and type hierarchy.

Example of implicit typecasting is when var c = 1.9 is added with var d= 8, For the answer 9.9 the var d is converted into float automatically as 8.0

'''
