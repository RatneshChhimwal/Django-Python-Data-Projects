# write a function:

'''
You are given a string containing numbers, alphabetic characters, and special characters.
Your task is to reverse the string while keeping the special characters in their original positions.

Example - Given string: 1um3br&el4#la, Solution: al4le&rb3#mu1
'''

def solution(string):
    alnum_list = []        # Step 1: Initialize an empty list for alphanumeric characters
    special_dict = {}      # Step 2: Initialize a dictionary for special characters and their indices

    # Step 3: Loop through the string, separating alphanumeric and special characters
    for i, e in enumerate(string):
        if e.isalnum():    # If the character is alphanumeric
            alnum_list.append(e)  # Add it to the alnum_list
        else:
            special_dict[i] = e   # Otherwise, store the special character's index and value in the dictionary

    # Step 4: Reverse the alphanumeric list
    alnum_list.reverse()

    # Step 5: Insert special characters back at their original indices
    for idx, char in special_dict.items():
        alnum_list.insert(idx, char)  # Insert special characters at their original indices

    # Step 6: Join the list back into a string and return the result
    return ''.join(alnum_list)

# Example
string = "r4a&n9e*>sh"
print(solution(string))  # Output: 4la3re&lb1#mu
