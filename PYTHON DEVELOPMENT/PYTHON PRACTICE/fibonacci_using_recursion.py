# We are tasked to create fibonacci series with the help of recursion

def fibonacci(n):
    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n
    else:
        # Recursive case: sum of the two preceding numbers in the series
        return fibonacci(n - 1) + fibonacci(n - 2)

# Generate the Fibonacci series up to a certain number of terms
num_terms = int(input("Enter the number of terms: "))

print("Fibonacci Series:")
for i in range(num_terms):
    print(fibonacci(i), end=" ")

"""

NOTE: In the above function, The fibonacci function has been recursively called inside its own definition,
So, if were to call the function as fibonacci(n), then inside the if-else loop itself the function
will recursively find values for lower values to calculate the fibonacci(n)
The recursive call will find the value of fibonacci(2) till fibonacci(n-1)

"""
