# 6. **Dictionary Merge**: Write a function to merge two dictionaries, combining values of common keys by summing them.

"""

Let's say the 2 dicts are 
dict1 = {'a':1,'b':2,'c':3,'d':4}
and
dict1 = {'c':3,'b':1,'e':1,'f':1}

Resultant required is

result_dict = {'a':1,'b':3,'c':6,'d':4,'e':1,'f':1}

"""

def combine_dicts(a,b):
    empty_dict = {}

    for i,j in a.items():
        empty_dict[i] = j
    for k,l in b.items():
        if k in empty_dict:
            empty_dict[k] +=l
        else:
            empty_dict[k] = l

    return empty_dict
    
a = {'a':1,'b':2,'c':3,'d':4}
b = {'c':3,'b':1,'e':1,'f':1}

print(combine_dicts(a,b))
