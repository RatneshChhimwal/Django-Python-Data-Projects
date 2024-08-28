def Sort_dict(input_dict):
    # Sort the dictionary by its keys
    sorted_keys = sorted(input_dict.keys())
    
    # Create a new empty dictionary
    sorted_dict = {}
    
    # Add items to the new dictionary in the sorted key order
    for key in sorted_keys:
        sorted_dict[key] = input_dict[key]

        """ NOTE: The code-line "sorted_dict[key] = input_dict[key]" is for adding a key-value pair to a dictionary,
        (dict['key'] = 'value'), Here value is being fetched by input_dict[key] """
    
    # Print the sorted dictionary
    print(sorted_dict)

# Example usage
input_dict = {12: "banana", 9: "apple", 3: "mango", 14: "orange"}
Sort_dict(input_dict)
