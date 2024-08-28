# Below, we have a dictionary 'ep' that contains the employee's performance out of 100 in correspondence with their IDs
# 'res' is a dictionary containing few more new employees

ep={11: 45, 12: 34, 13: 75, 14: 68, 15: 68}
res={16:87, 17:92}

print(ep.get(12))                               # 'get' method is used to extract the value from the dictionary against the argument keyword

ep.update(res)                                  # 'update' method is used to update an existing dictionary with values from another dictionary

res.clear()                                     # 'clear' method is used to clear out a dictionary of its key-value pairs

ep.pop(12)                                      # 'pop' method is used to pop out a 'value' from the dictionary against the argument keyword

del ep[13]                                      # 'del' method is used to delete the key-value pair from the dictionary against the argument keyword

print(ep.get())