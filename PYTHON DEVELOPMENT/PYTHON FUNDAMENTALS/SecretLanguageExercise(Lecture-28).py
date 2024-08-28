# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains at least 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
# reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# APPROACH:

"""

First I will create 2 options, CODE or DECODE
Then, Suppose if chosen CODE, I will let the user input a string
Then, I will use 'for' loop to go over the words of the string one by one
Then as the exercise says, I will check the length of the word stored in 'i' of 'for' loop and perform the required encryption
once encrypted, I will store that new word in a last variable which will have the whole encrypted string

"""

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import random

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

choice = input("Do you want to 'CODE' or 'DECODE'\n").upper()
if choice == "CODE":

    Codestr = input("Enter the string to be encrypted below\n")

    # The below line is vital as it allows word-by-word iteration within the 'for' loop using the split method, rather than each character

    Codewords = Codestr.split()

    # If we simply used 'for' loop on 'Codestr' before using 'split', The loop would have iterated over each character of the input string

    for i in Codewords:
        if len(i) >= 3:
            first_letter = i[:1]                                            # 'first_letter' contains the first letter of the word stored in 'i' during an iteration
            letters = ['abc', 'bac', 'cba']                                 # List 'letters' contains the random words we want to put at start & end for encryption
            random_words = random.choices(letters)                          # The variable 'random_words' is used to store the random word chosen by using 'choice' method
            print(random_words[0] + i + first_letter + random_words[0])     # The reason we concatenate 'random_words[0]' because 'random_words' stores a list and not a str
        else:
            reverse = i[::-1]
            print(reverse)

elif choice == "DECODE":
    Decodestr = input("Enter the code you want to decode\n")

    # The below line is vital as it allows word-by-word iteration within the 'for' loop using the split method, rather than each character

    Decodewords = Decodestr.split()

    # If we simply used 'for' loop on 'Decodestr' before using 'split', The loop would have iterated over each character of the input string

    for i in Decodewords:
        if len(i) >= 3:
            j = i[:-3]                                      # 'j' contains the last 3 letters of the word stored in 'i'
            k = j[3:]                                       # 'k' contains the first 3 letters of the word stored in 'j'
            last_appended_value = k[len(k)-1:len(k)]        # 'last_appended_value' contains the last letter of the word stored in 'k'
            k=k[:-1]                                        # Here we removed the last letter from 'k' because we are appending the sae=me at the start
            print(last_appended_value + k)                  # Concatenating the resultant string
        else:
            reverse = i[::-1]
            print(reverse)

else:
    print("Choose one of the options only")


