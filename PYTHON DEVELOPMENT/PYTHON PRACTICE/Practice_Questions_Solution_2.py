# 2. **Factorial Using Recursion**: Implement a recursive function to calculate the factorial of a number.

def factorial_check(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_check(n-1)

print(factorial_check(3))

        

