# 5. **Fibonacci Series**: Generate the first `n` numbers in the Fibonacci sequence using iteration.

def fibonacci(n):
    fib_sequence = []
    
    # First two Fibonacci numbers
    a, b = 0, 1
    
    for _ in range(n):
        fib_sequence.append(a)  # Add the current number to the list
        a, b = b, a + b  # Update 'a' and 'b' to the next two Fibonacci numbers
        
    return fib_sequence

n = 10  # Generate first 10 Fibonacci numbers
print(fibonacci(n))