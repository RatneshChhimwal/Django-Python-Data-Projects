def bubble_sort(input_list):
    n = len(input_list)  # Get the length of the list
    
    # Traverse through all elements in the list
    for i in range(n):
        
        # Flag to detect if any swapping happened in this pass
        swapped = False
        
        # The last i elements are already sorted, so no need to check them
        for j in range(0, n - i - 1):
            
            # If the current element is greater than the next element, swap them
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                swapped = True  # Set the flag to True to indicate a swap happened
        
        # If no elements were swapped, the list is already sorted, so we can stop
        if not swapped:
            break
    
    return input_list

# Calling the function:

sorted_list = bubble_sort([21,45,32,13,43,26])
print("Sorted list:", sorted_list)


# EXPLANATION:

"""

Suppose, We have an unsorted list [7,4,5,2,6,9].
We find out the length of the list (in this case, length = 6)
Then we start a for loop with 'i' on the list,
In the first iteration the value of i is 7 at the index 0,
holding the value of i=7, We move further into the nested loop
with j in range (0, n-i-1), What this does is, As the length for above list was 6,
it makes loop for j as "j in range (0,6-0-1)" which is "j in range (0,5)"
Now, inside the nested 'j' loop, We compare adjacent values,
As, "input_list[j] > input_list[j + 1]"
This calculates the value of input_list[j] with value of input_list[j+1]
For first iteration on our list [7,4,5,2,6,9], 'j' = 0
So, if input_list[0] > input_list[1], then,
input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j] and Swap the values.

* NOTE: For every iteration of 'j' loop, the range at which we are performing comparison is like:
        "for j in range(0,5)" means "j" loop over from index "0" till "4"
        So, value at index 0 is compared with value at index 1, then
        value at index 1 is compared with value at index 2
        value at index 2 is compared with value at index 3
        value at index 3 is compared with value at index 4

        Ultimately pushing the largest value at the end for each iteration

"""

