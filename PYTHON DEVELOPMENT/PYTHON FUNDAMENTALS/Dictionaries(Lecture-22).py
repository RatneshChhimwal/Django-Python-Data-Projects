# DICTIONARIES:

"""

Dictionaries in Python are data structures that store key-value pairs, allowing efficient access to values by unique keys.
They are unordered, mutable, and versatile for various data storage needs.

SYNTAX: Name of the dictionary={'Keyword':'Value','Keyword':'Value','Keyword':'Value'}

"""

dic = {'Roll no.': 18, 'Name': 'Ratnesh','Address': 'Vaishali'}

print(dic['Roll no.'])
print(dic)

# To access all keys and their values at once, We can also write the below:

print(dic.keys())             # Syntax: print(Name of the dictionary.keys())

# To iterate all the keys separately, we use 'for' loop as we know, For dictionaries, the syntax is as below:

for key in dic.keys():        # for 'variable' in 'dictionary.keys()':
    print(key)                # print(variable)

for val in dic.keys():        # for 'variable' in 'dictionary.keys()':
    print(dic[val])           # print(dictionary[variable]) here prints the value of the corresponding key because of [] square brackets


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 'See the below f-string' # IMPORTANT:

for key in dic.keys():
    print(f"The key name is {key}")

for val in dic.keys():
    print(f"The value corresponding to the key {val} is {dic[val]}")








