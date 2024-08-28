""" 
We are tasked to find the missing number from an array of consecutive numbers,
Suppose, User inputs a list [1,2,4,5,6,7], then we have to find the missing number as 3

"""

def missing_number():
    # Get the input list as a comma-separated string
    input_list = input("Enter the list of consecutive numbers (comma-separated): ")
    
    # Convert the input string to a list of integers
    list_conversion = list(map(int, input_list.split(',')))

    # ** The 'map()' function applies a given function to all items in an iterable (like a list). **
    
    # Find the maximum number in the list to determine the range
    n = len(list_conversion) + 1  # We expect one number to be missing
    
    # Calculate the expected sum of numbers from 1 to n
    expected_sum = (n * (n + 1)) // 2

    # ** We have used floor division ('//') to ensure that you get an integer result, as the single slash /, the division produces a floating-point number **
    
    # Calculate the actual sum of the numbers provided
    actual_sum = sum(list_conversion)
    
    # The missing number is the difference between the expected sum and the actual sum
    missing_number = expected_sum - actual_sum
    
    print(f"The missing number is: {missing_number}")

missing_number()
