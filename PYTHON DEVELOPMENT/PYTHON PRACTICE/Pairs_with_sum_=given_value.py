"""
We are tasked to find out pairs from a array of numbers whose sum equals to the given value.
So, Let's say given number (x=13)
and Array given is ( y=[1,2,3,4,5,6,7,8,9,10] )
then pairs with sum equals to 13 would be (3,10),(4,9),(5,8),(6,7) 

"""

def pair_sum_equals_to_given_number():
    # Taking input from the user
    Value = int(input("Enter the value to find the sum of pairs for:\n"))
    Input_array = input("Enter the array (comma-separated):\n")

    # Convert the input string to a list of integers
    Resultant_list = list(map(int, Input_array.split(',')))

    # Sort the list
    Resultant_list.sort()

    # Initialize pointers
    left = 0
    right = len(Resultant_list) - 1

    # Loop through the list to find pairs
    while left < right:
        current_sum = Resultant_list[left] + Resultant_list[right]

        if current_sum == Value:
            print(f"The pair is {Resultant_list[left]} and {Resultant_list[right]}")
            left += 1
            right -= 1
        elif current_sum < Value:
            left += 1
        else:
            right -= 1

# Call the function
pair_sum_equals_to_given_number()
