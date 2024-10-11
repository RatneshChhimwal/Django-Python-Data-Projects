# 9. **Capitalize Every Word**: Write a function that capitalizes the first letter of every word in a string.

list = []

def new(a):
    words = a.split(" ")
    for i in words:
        list.append(i[0].upper() + i[1:])
    result = " ".join(list)
    return result

a = "This is a great evening"


print(new(a))