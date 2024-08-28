'''
A recursive function in Python is a function that solves a problem by breaking it down into smaller,
similar sub-problems and repeatedly calling itself to solve those sub-problems until a base case is reached.
'''


'''
In the below code, We have called the func 'factorial' inside the definition of the function itself,
As factorial of a value 'n' is equal to 'n' multiplied by factorial of the preceding value i.e. '(n-1)'
'''

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(4))



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# EXERCISES:

'''
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
Your task is to write a recursive function to calculate the nth number in the Fibonacci sequence.
'''

def fibonacci(b):                                       # We define a func 'fibonacci' that takes an argument 'b'
    if b==0:                                            # We define the predefined/known/default values first and define what they return
        return 0
    elif b==1:                                          # We define the predefined/known/default values first and define what they return
        return 1
    else:
        return (fibonacci(b-1))+(fibonacci(b-2))

print(fibonacci(6))

# **** NOTE: The function knows the values for fibonacci series at index '5' & '4' by doing the calculation for fibonacci[2], then fibonacci[3] and so on. *********


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------



# EXERCISE-2:

'''Write a recursive function that calculates the sum of the digits that exist between the 2 digit input (positive integer).
For example, if the input is 15, the function should return 15 (1 + 2 + 3 + 4 + 5), or if the input is 37, the function should return 25 (3 + 4 + 5 + 6 + 7)'''


def sum_of_digits(c):
    if c in range(0,10):
        return c
    else:
        c_str=str(c)
        first_digit = c_str[0]
        second_digit = c_str[1]

        # Convert the characters back to integers

        first_digit_as_int = int(first_digit)
        second_digit_as_int = int(second_digit)

        digit_sum = sum(range(first_digit_as_int, second_digit_as_int + 1))

        return digit_sum

result = sum_of_digits(37)
print(result)