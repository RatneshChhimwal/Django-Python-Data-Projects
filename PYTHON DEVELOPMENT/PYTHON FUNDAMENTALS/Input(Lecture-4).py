a = input("Enter your name: ") # Variable 'a' will be assigned the value input by the user
print("My name is", a)

x = input("Enter first number: ")
y = input("Enter second number: ")
print(x + y) # Know that the following print function will concatenate the numbers instead of addition as the default input type for python is string.

print(int(x) + int(y)) # To avoid concatenation and use addition, We can typecast the values into integer type as so.

# The above typecasting can be avoided by defining the input type while taking input only as below:

'''

x = int(input("Enter first number: "))  # Here we defined the input type as int right before the input function so the arithmatic functions can now be used directly.
y = int(input("Enter second number: ")) # Here we defined the input type as int right before the input function so the arithmatic functions can now be used directly.

'''