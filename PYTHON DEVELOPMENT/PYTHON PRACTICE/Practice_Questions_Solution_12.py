# 12. **Sum of Subarrays**: Write a function that returns all possible subarrays from a list:

"""

Example
Input:
List: [1, 2, 3]

Output:
Subarrays and their sums:

Subarray: [1]
Subarray: [2]
Subarray: [3]
Subarray: [1, 2]
Subarray: [2, 3]
Subarray: [1, 2, 3]

"""

def get_subarrays(arr):
    # Empty list to store subarrays
    result = []
    
    # Outer loop: This loop picks the starting point of each subarray
    for start in range(len(arr)):
        
        # Inner loop: This loop picks the ending point of each subarray
        for end in range(start, len(arr)):
            
            # Get the subarray using slicing and append it to the result
            subarray = arr[start:end + 1]
            result.append(subarray)
    
    return result

# Example usage:
arr = [1, 2, 3]
print(get_subarrays(arr))