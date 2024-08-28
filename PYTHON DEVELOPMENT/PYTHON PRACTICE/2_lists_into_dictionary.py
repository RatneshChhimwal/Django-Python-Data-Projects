""" 
We are tasked to map/convert 2 lists into a dictionary.
Say, we have list1 = [1,2,3] and list2 = ["one", "two", "three"],
We have to create a dictionary :
dict = {1:"one", 2:"two", 3:"three"}

"""

def lists_to_dict():
    # Input lists as comma-separated strings
    list1 = input("Enter the list to be used as keys (comma-separated):\n")
    list2 = input("Enter the list to be used as values (comma-separated):\n")

    # Convert input strings to lists by splitting at commas
    list1 = list1.split(',')
    list2 = list2.split(',')

    # Strip any extra whitespace from each item in the list
    list1 = [item.strip() for item in list1]
    list2 = [item.strip() for item in list2]

    # Create a dictionary by zipping the two lists together
    result = dict(zip(list1, list2))
    print(result)

lists_to_dict()
