# 14. **Two Sum Problem**: Given a list of numbers and a target sum, return indices of two numbers that add up to the target.

'''

List = [1,2,3,4,5,6,7,8,9]
Sum_required = 8

'''

def sum_indices(a, sum_required):
    final_list = []
    for e,i in enumerate(a):
        for f,j in enumerate(a):
            if i+j == sum_required:
                final_list.append([e,f])
    return final_list

a = [1,2,3,4,5,6,7,8,9]
sum_required = 8
    
print(sum_indices(a, sum_required))