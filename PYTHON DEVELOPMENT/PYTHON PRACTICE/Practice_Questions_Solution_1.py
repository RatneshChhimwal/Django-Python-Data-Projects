# 1. **String Palindrome**: Write a function to check if a given string is a palindrome, ignoring spaces and case.

def palindrome(string):
    refined_string = ""
    for i in string:
        if i != " ":
            i = i.lower()
            refined_string = refined_string + i
    if refined_string == refined_string[::-1]:
        print(f"The given string {string} is a palindrome as it is equal to {refined_string}")
    else:
        print("NO")


string = "Fal a f"

palindrome(string)