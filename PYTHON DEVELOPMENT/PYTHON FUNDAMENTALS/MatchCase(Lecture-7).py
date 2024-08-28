# MATCH CASE STATEMENTS:

'''

A match case statement, introduced in Python 3.10, is used to perform pattern matching on values.
It allows you to compare a value against multiple patterns and execute code based on the first pattern that matches the value.

'''

# NOTE: WHILE TRADITIONAL IF-ELSE OR NESTED IF-ELSE STATEMENTS CAN SUBSTITUTE MATCH CASE, MATCH CASE ENHANCES READABILITY. **********

# BELOW IS AN EXAMPLE OF CODE USING MATCH CASE FOLLOWED BY EXPLANATION FOR EACH STEP:

x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("x is 4")

    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)


'''

Question: Write a Python program that takes a numeric grade as input (e.g., 1 to 100)
and uses match case statements to determine the corresponding letter grade based on the following rules:

90-100: "A"
80-89: "B"
70-79: "C"
60-69: "D"
Below 60: "F"
Your program should take the input grade and print the corresponding letter grade. Use match case statements to handle each grade range.

'''

Marks=int(input("Enter marks for the student (1 to 100)"))

if 1<Marks<100:
    pass                            # 'pass' is used to process the code further only if the 'if' condition is satisfied

    match Marks:
        case _ if 90<Marks<100:     # Here we have defined multiple 'if' conditions with 'case' statements only because we had to define range of marks
            print("Grade is A")     # We could've directly used 'case' is we had to match particular values only
        case _ if 80<Marks<90:
            print("Grade is B")
        case _ if 70<Marks<80:
            print("Grade is C")
        case _ if 60<Marks<70:
            print("Grade is D")
        case _ if 50<Marks<60:
            print("Grade is E")
        case _:
            print("Better luck next time")

else:
    print("Kindly enter marks between 1 and 100 only")
