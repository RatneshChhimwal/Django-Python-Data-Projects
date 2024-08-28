# ARITHMETIC OPERATORS:

'''

Operator	Operator_Name	    Example     Return Value

+	        Addition	        15+7        22
-	        Subtraction	        15-7        8
*	        Multiplication	    5*7         35
**	        Exponential	        5**3        125
/	        Division	        5/3         1.66
%	        Modulus	            15%7        1 (Gives the remainder)
//	        Floor Division	    15//7       2 (Gives the quotient)

'''


# CALCULATOR FROM PYTHON:

a=int(input("Enter 1st number"))        # We used 'int' to convert the string input from user to integer first as we further need to perform addition on those inputs
b=int(input("Enter 2nd number"))        # We used 'int' to convert the string input from user to integer first as we further need to perform addition on those inputs

add=a+b                                 # We created a variable 'add' which stores the value of sum of 'a' & 'b'
print("The addition of the above 2 numbers is", add)

sub=a-b                                # We created a variable 'sub' which stores the value of subtraction of 'a' & 'b'
print("The subtraction of the above numbers is", sub)




# IMPLEMENT A NUMBER GUESSING GAME WHERE THE COMPUTER SELECTS A RANDOM NUMBER, AND THE USER TRIES TO GUESS IT.
import random
Num1=random.randint(1,10)
Num2=int(input("Guess the number"))

if Num1==Num2:
    print("You have guessed the correct number")
else:
    print("The number generated was", Num1)





# BUILD A PROGRAM THAT CONVERTS UNITS LIKE TEMPERATURE (E.G., CELSIUS TO FAHRENHEIT)

TempCal=int(input("Enter the temprature in celcius"))

TempFar = (TempCal * 9/5) + 32

print("The temprature in far is", TempFar)

