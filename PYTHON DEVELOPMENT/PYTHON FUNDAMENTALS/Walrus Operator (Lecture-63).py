"""

The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable within an expression.
The Walrus Operator is represented by the := syntax and can be used in a variety of contexts including while loops and if statements.

Here's an example of how you can use the Walrus Operator in a while loop:

"""

numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0:
    print(numbers.pop())

"""
In this example, the length of the numbers list is assigned to the variable n using the Walrus Operator.
The value of n is then used in the condition of the while loop, so that the loop will continue to execute until the numbers list is empty.
"""

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# The below program keeps asking the user to input foods they like until the user enters "quit." It then displays the list of entered foods.


foods = list()

while True:
    food = input("What food do you like?: ")

    if food == "quit":
        break

    foods.append(food)

print(foods)

# The same could be simplified as below with the help of 'Walrus' operator

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)


"""
The primary benefit is that you can both assign a value to a variable and use that value in an expression in a single line of code.
"""

n=3
square= n*n
print(square)

# With walrus operator

n = 5
print(square := n * n)


"""
In the second example, the walrus operator is used to assign the result of n * n to the variable square
while simultaneously using it as an argument to print().
This makes the code more concise.
"""
