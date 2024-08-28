'''

In python, anything that you enclose between single or double quotation marks is considered a string.
A string is essentially a sequence or array of textual data. Strings are immutable in sense they can not be altered implicitly.

name = "Ratnesh"
print("Hello, " + name) # This will print "Hello Ratnesh", Concatenating Hello with Var 'name'

'''

# To write a whole paragraph or multiple lines of string without the use of escape sequences and assign it to a variable, We can use triple 'single/double' quotes as below:

St="""Here I have assigned a string
with multiple lines to a 
variable St without the use of escape sequence
backslash n for next line """

print(St)

'''

In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.
Square brackets can be used to access elements of the string. Example below:

'''

Name="Ratnesh"
print(Name[0]) # This prints the letter 'R' from the string 'Ratnesh' as that letter is assigned the index 'zero (0)'
print(Name[:4]) # This prints the sliced string 'Ratn' where index zero is included while the index '4' is excluded
print(Name[4:]) # This prints the sliced string 'esh' from index '4' to the last index '6'
print(Name[2:5]) # This prints the sliced string 'tne' where index '2' is included while the index '5' is excluded

# Note: We can slice and print all characters WRT the index they hold, but for large strings e.g. the string assigned to var 'St' above, doing so would be difficult.
# So we instead use the 'for' loop, As below:

for characters in St: # Here we have defined a var 'characters', The 'for' loop is iterating each held index in the string assigned to var 'St' and storing it back in var 'characters' for printing
    print(characters)


# To know the length of a string we use 'len' function, As below:

print(len(Name)) # This prints the length of the variable 'Name' as '7'


# Whenever 'negative' numbers are put inside a string slice print function, the interpreter automatically adds the 'len(variable)' before it, e.g. below:

print(Name[:-3]) # This will be converted to print(Name[:len(Name)-3]), Which becomes print(Name[:7-3]) i.e. print(Name[:4])


# IMMUTABILITY OF STRINGS:

# Suppose a variable 'd' is assigned the string 'PyThoN' with few capital letters and few small letters

d = "PyThoN"

# Whatever functions will be performed upon the above strings, can would not be updated in the formal/main variable, As below:

print(d.upper()) # This would return 'PYTHON'
print(d.lower()) # This would return 'python'

# Both the above functions but have created new strings, whereas the var 'd' still holds the string 'PyThoN' with few capital letters and few small letters.



# STRING METHODS: ----------------------------------- ***** -------------------------------------- IMPORTANT --------------------------

'''

Python provides a set of built-in methods that we can use to alter and modify the strings, Few of the string methods are listed below along with the definition:

(1) upper() :
The upper() method converts a string to upper case.

Example:
str1 = "AbcDEfghIJ"
print(str1.upper())

Output:
ABCDEFGHIJ

(2) lower()
The lower() method converts a string to lower case.

Example:                                    
str1 = "AbcDEfghIJ"
print(str1.lower())

Output:
abcdefghij

(3) strip() :
The strip() method removes any white spaces before and after the string.

Example:
str2 = " Silver Spoon "
print(str2.strip)

Output:
Silver Spoon ------ without spaces


(4) replace() :
The replace() method replaces all occurrence of a string with another string. Example:

str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))

Output:
Silver Moon

(5) split() :
The split() method splits the given string at the specified instance and returns the separated strings as list items.

Example:
str2 = "Silver_Spoon"
print(str2.split("_"))      #Splits the string at the underscore "_".

Output:
['Silver', 'Spoon']

(6) center() :
The center() method aligns the string to the center as per the parameters given by the user.

Example:
str1 = "Welcome to the Console!!!"
print(str1.center(50))

Output:
            Welcome to the Console!!!

We can also provide padding character. It will fill the rest of the fill characters provided by the user.

Example:
str1 = "Welcome to the Console!!!"
print(str1.center(50, "."))

Output:
............Welcome to the Console!!!.............

(7) count() :
The count() method returns the number of times the given value has occurred within the given string.

Example:
str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr)

Output:
4

(8) index() :
The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.

Example:
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))

Output:
13

(9) islower() :
The islower() method returns True if all the characters in the string are lower case, else it returns False.

Example:
str1 = "hello world"
print(str1.islower())

Output:
True

Similarly 'isupper()' method returns True if all the characters in the string are upper case, else it returns False.

(10) startswith() :
The endswith() method checks if the string starts with a given value. If yes then return True, else return False.

Example :
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

Output:
True

'''

