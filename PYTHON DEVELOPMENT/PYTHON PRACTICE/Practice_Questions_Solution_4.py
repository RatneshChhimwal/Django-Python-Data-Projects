# 4. **List Flattening**: Write a function that takes a nested list and returns a flattened list.

"""

Nested list = [1,2,[3,4,5],[6,7,8,9],10]

Returned_list = [1,2,3,4,5,6,7,8,9,10]


"""

def list_flattener(nested_list):
    returned_list=[]
    for i in nested_list:
        if isinstance(i, list):
            returned_list.extend(i)
        else:
            returned_list.append(i)
    return returned_list

nested_list = [1,2,[3,4,5],[6,7,8,9],10]

print(list_flattener(nested_list))