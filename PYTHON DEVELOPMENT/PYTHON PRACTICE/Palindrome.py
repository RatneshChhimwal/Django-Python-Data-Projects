# We are tasked to create a function that checks if a given string is palindrome or not

def palindrome():
    input_string = input("Enter the string you want to check for palindrome\n")

    Resultant_string = input_string.upper()

    if Resultant_string == Resultant_string[::-1]:
        print("Given string is a palindrome")
    else:
        print("Given string is not a palindrome")

palindrome()


# ALTERNATE: ---------------------------------------------------------------------------------------------------------------------------------

def palindrome_alternate():
    input_string = input("Enter the string you want to check for palindrome\n")

    Resultant_string = input_string.upper()

    n = len(Resultant_string)
    x = 0

    for i in range(n):
        if Resultant_string[i] != Resultant_string[n-i-1]:
            x = 1
            break
    if x == 0:
        print("Given string is a palindrome")
    else:
        print("Given string is not a palindrome")


palindrome_alternate()