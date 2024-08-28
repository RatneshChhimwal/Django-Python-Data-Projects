a = int(input("Enter your age: "))
print("Your age is:", a)

# Conditional operators
# >, <, >=, <=, ==, !=
# print(a>18)  # If the user input is 18, then this would return FALSE
# print(a<=18) # If the user input is 18, then this would return TRUE
# print(a==18) # If the user input is 18, then this would return TRUE
# print(a!=18) # If the user input is 18, then this would return FALSE

if a > 18:                     # The following condition checks if the input value for var 'a' is more than 18, If yes,then prints the string below.
    print("You can drive")     # The 'Space' before the print statement suggests that the string is defined inside the 'If' condition (INDENTATION).
else:                          # The following string is printed in cases the 'If' condition is not satisfied.
    print("You cannot drive")  # The 'Space' before the print statement suggests that the string is defined inside the 'else' condition (INDENTATION)


# DEFINITION OF IF-ELSE CONDITIONAL FUNCTION:

'''

An if-else condition is a decision-making structure that allows you to execute different blocks of code based on a specified condition.
You start with an "if" statement, followed by a condition in parentheses.
If that condition is true, the code within the indented block under "if" is executed; otherwise,
the code under "else" (if provided) is executed.

'''

# Another example of if-else program

FirstName=input("Enter your first name")
print("Your name is ", FirstName)

if len(FirstName)>7:
    print("That is a long name")
else:
    print("That is a short name")


#---------------------------------------------------------------------------------------------------------------------------------------------------------




# "if-elif-else" CONDITIONAL FUNCTIONS:

Lastname= input("Enter your last name")

if len(Lastname)<=4:
    print("Your last name is of small length ")

elif 4<len(Lastname)<=8:  # elif 4 < len(Lastname) <= 8: checks if the length of Lastname is greater than 4 and less than or equal to 8.
    print("Your last name is of medium length")

else:
    print("No last name has been entered")


# --------------------------------------------------------------------------------------------------------------------------------------------------------

# NESTED if-else CONDITIONAL STATEMENT

'''

Question: Write a Python program that takes an integer as input and determines if it's even or odd.
If it's even, check if it's also a multiple of 4 and print the result accordingly.
You can use nested if-else statements to first check if the number is even or odd,
and then within the even branch, check if it's a multiple of 4 and print the appropriate message.

'''


UserIn=int(input("Enter a number"))

if (UserIn)%2==0:

    if (UserIn)%4==0:
        print("The number is even as well as a multiple of 4")   # This nested 'if' condition checks for divisibility by '4' when the initial 'if' condition of an even value is true.

    elif (UserIn)%4!=0:
        print("The number is even but is not a multiple of 4")

elif (UserIn)==0:
    print("The number is zero")
else:
    print("The number is odd")


# ************* NESTED IF-ELSE IS USED WHEN WE WANT TO CHECK FOR MULTIPLE SUB-CONDITIONS ONCE ONE OF PRIMARY CONDITIONS ARE SATISFIED.
