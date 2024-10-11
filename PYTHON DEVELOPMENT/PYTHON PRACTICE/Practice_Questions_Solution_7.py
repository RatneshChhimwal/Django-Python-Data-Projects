# 7. **Find Duplicates in a List**: Write a function that identifies duplicate values in a list.

def find_duplicates(a,b):
    combined_list = []
    duplicates = []

    for i in a:
        combined_list.append(i)
    for j in b:
        if j in combined_list:
            duplicates.append(j)
        else:
            combined_list.append(j)
    return duplicates

a = [1,2,3,4,5,8]
b = [2,5,6,7,8,1]

print(f" The duplicate values are {find_duplicates(a,b)}")