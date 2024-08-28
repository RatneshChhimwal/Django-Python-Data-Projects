"""
We are tasked to create an infinite fibonacci series.

We use the concept of a generator where instead of return we use the keyword 'yield' 
to extract the value of a variable after each execution

"""


def fibonacci():
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    
    # Infinite loop to keep generating Fibonacci numbers
    while True:
        # Yield the current value of 'a' and pause execution
        yield a
        
        # Update 'a' and 'b' for the next Fibonacci number
        # 'a' becomes the old 'b', and 'b' becomes the sum of old 'a' and old 'b'
        a, b = b, a + b

# Create a generator object 'f1' from the fibonacci() generator function
f1 = fibonacci()

# Generate and print the next Fibonacci number in sequence
print(next(f1))  # Outputs: 0 (First Fibonacci number)

# Generate and print the next Fibonacci number in sequence
print(next(f1))  # Outputs: 1 (Second Fibonacci number)

# Generate and print the next Fibonacci number in sequence
print(next(f1))  # Outputs: 1 (Third Fibonacci number)

# Generate and print the next Fibonacci number in sequence
print(next(f1))  # Outputs: 2 (Fourth Fibonacci number)

# Generate and print the next Fibonacci number in sequence
print(next(f1))  # Outputs: 3 (Fifth Fibonacci number)

# Generate and print the next Fibonacci number in sequence
print(next(f1))  # Outputs: 5 (Sixth Fibonacci number)

# Generate and print the next Fibonacci number in sequence
print(next(f1))  # Outputs: 8 (Seventh Fibonacci number)
