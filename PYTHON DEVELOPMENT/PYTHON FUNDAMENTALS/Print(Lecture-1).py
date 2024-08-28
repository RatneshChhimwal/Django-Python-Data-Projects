print("hello world")

# To print multiple lines of codes line by line we rather type script then to write print commands again and again

print("This will come in the \"first line\" \nand this will be printed in the next\t we can use backslash \\ in the string too by using double backslash escape sequence")  # Escape sequences

# BELOW ARE ALL THE BASIC ESCAPE SEQUENCES AND THEIR USAGE:

""" \n - Newline:
Use: Inserts a newline character to start a new line of text.

\t - Tab:
Use: Inserts a tab character to add horizontal spacing.

\\ - Backslash:
Use: Escapes a backslash character to include it in the string.

\" - Double Quote:
Use: Escapes a double quote character to include it in double-quoted strings.

\' - Single Quote:
Use: Escapes a single quote character to include it in single-quoted strings.

\b - Backspace:
Use: Moves the cursor back one space, erasing the character to the left. """

# A print statement can be used to print multiple values at once, and we can also define seperator (default-SPACE) and value we want to print at the end, Example below:

print("Ratnesh", 18, "03 ", sep="_", end="1999\n")



# VARIABLES: -------------------------------------------------------------------------------------------------------------------------------------------------------------

# Variable is like a container that holds data. Creating a variable is like creating a placeholder in memory and assigning it some value.

a = 123  # Integer data type
print(a)  # This will print 123 instead of the letter 'a' as we have already defined the value stored in the variable a.

b = "Python"  # String data type
print(
    b)  # This will print 'Python' instead of the letter 'b' as we have already defined the string stored in the variable b.

# To concatenate 2 different data types, we need to convert them into similar data type first, Example below:

var1 = 12
var2 = "twelve"

# If we want to return the string 'Twelve12' then the function would be as below

Var3 = var2 + str(var1) # We converted the int type value stored in var1 to string type before concatenation
print(Var3)

# We can also know the type of data stored in a particular variable by using the type(variable name) function, Example below:

print(type(Var3))