"""

The shorthand syntax can be a convenient way to write simple if-else statements,
especially when you want to assign a value to a variable based on a condition.
However, it's not suitable for more complex situations where you need to execute multiple statements or perform more complex logic.
In those cases, it's best to use the full if-else syntax.

"""

# SYNTAX TO SHORT-HAND 'if-else'

# result = value_if_true if condition else value_if_false

# EXAMPLE:

a=34
b=39

print("A is bigger") if a>b else print("B is bigger") if a<b else print("A and B are equal")

# In the above example, We have simply defined a continuous if-elif-else structure going left to right

# ----------------------------------------------------------------------------------------------------------------------

# USE OF 'result = value_if_true if condition else value_if_false'

c = 9 if a<b else "10"

# Here 'c' is 'result'
# '=9' is the 'value_if_true'
# 'a<b' is the 'if' condition for assigning "c=9"
# "10" for 'c' is the 'value_if_false'

print(c)


