# We are tasked to find common letters between 2 strings:

def common_letters():
    string1 = input("Enter first string\n")
    string2 = input("Enter second string\n")

    Distinct_letters_string1 = set(string1)
    Distinct_letters_string2 = set(string2)

    common = Distinct_letters_string1 & Distinct_letters_string2  # The '&' operator is used to extract the common values from sets
    print(common)

common_letters()