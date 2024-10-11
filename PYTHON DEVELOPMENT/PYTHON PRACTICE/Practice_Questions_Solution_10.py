# 10. **Find the Intersection of Two Lists**: Write a function that returns the intersection of two lists.

empty_list = []

intersection_list = []

def intersection(a,b):
    for i in a:
        empty_list.append(i)
    for j in b:
        if j in empty_list:
            intersection_list.append(j)
    return intersection_list

a = [1,2,3,4,5]
b = [3,4,5,6,7]

print(intersection(a,b))