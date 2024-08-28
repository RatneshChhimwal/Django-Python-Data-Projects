# We are tasked to find the frequency of each word in an input string

def frequency_words():
    input_string = input("Enter the input string\n")
    list_of_words = input_string.split()
    print(list_of_words)

    empty_dictionary = {}
    
    for word in list_of_words:
        if word in empty_dictionary:
            empty_dictionary[word] += 1 # Initialize the word count to 1 
            # empty_dictionary[word] = 1 is setting the value of a particular key as 1 in the dictionary
        else:
            # Increment the word count
            empty_dictionary[word] = 1

    print(empty_dictionary)

frequency_words()
