# F-STRINGS:

'''
F-strings in Python are a way to easily put values or variables into a sentence or text.
You just need to add an 'f' before the text and put the values inside curly braces {} where you want them to appear.
Python will replace those curly braces with the actual values when you use the string.
It's like filling in the blanks in a sentence with real words or numbers.
'''

# A LITTLE IN_DEPTH DEFINITION IS BELOW:

'''

F-strings (formatted string literals) in Python are a way to create strings that include dynamic expressions or variables within them.
They are denoted by an 'f' or 'F' prefix before the string and allow you to embed Python expressions inside curly braces {} within the string.
When the string is evaluated, these expressions are replaced with their corresponding values.
'''

# EXAMPLES:

letter = "Hey my name is {0} and I am from {1}"  # Here we have a variable 'letter' i.e. assigned a string 'Hey my name is {1} and I am from {0}'

# In the above string the curly braces are used so that we can update the string later on with the values of the variable 'name' & 'country'

country = "India"                                # We define the variable 'country'
name = "Harry"                                   # We define the 2nd variable 'name'

print(letter.format(name, country))        # We define the format as 'print(Variable assigned the string.word'format'(Variables that are to be put in the string))'

print(f"Hey my name is {name} and I am from {country}")  # We print the f-string along with the name of the variables we want to put in it.

print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
