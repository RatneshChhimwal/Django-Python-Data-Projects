# 3. **Count Vowels in a String**: Write a function to count the number of vowels in a given string.

def count_vowels(string):
    list_of_vowels = ['i','e','a','o','u']
    count = 0
    for i in string:
        if i in list_of_vowels:
            count +=1
    print(f"Their are {count} vowels in the provided string")

count_vowels("Ratnieouesh")