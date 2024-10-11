# 13. **Longest Common Prefix**: Write a function to find the longest common prefix among a list of strings.

'''

So, if list is like 
a = ["flower", "flow", "flight"]
the common prefix would be common_prefix = ["fl"]

pehle list li
uske words pe loop chalata hun
to i hogya = "flower"
fir ek aur loop chalata hun nested from i till end
To j ki value hogyi "flow"
fir i[]

'''

a = ["flower", "flow", "flight"]

# Start by assuming the first word is the common prefix
common_prefix = a[0]

def find_common_prefix(a):
    global common_prefix  # Use global to modify the variable outside the function

    # Iterate over each word in the list starting from the second word
    for word in a[1:]:
        # Keep reducing the common prefix until the word starts with it
        while not word.startswith(common_prefix):
            # Remove the last character of the common prefix
            common_prefix = common_prefix[:-1]
            # If the common prefix becomes empty, return an empty string
            if common_prefix == "":
                return ""
    
    # Return the common prefix once we've checked all words
    return common_prefix

# Call the function and print the result
print(find_common_prefix(a))  # Output: "fl"
