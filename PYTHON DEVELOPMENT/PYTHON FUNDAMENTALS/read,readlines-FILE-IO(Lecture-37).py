# readline() Method:

"""
The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.
The readline() method reads all the lines of the file and returns them as a list of strings.
"""

#**************** IMPORTANT ************************ IMPORTANT ************************************************************************************************************

f= open("Use-Lecture-37.txt",'r')                       # We created a var 'f' and assigned it the file 'Use-Lecture-37.txt' using 'open()' func in 'r' (read) mode
i=0                                                     # We created another variable 'i' which holds the value '0' here

while True:                                             # We started a 'while' loop

    marks = f.readline()                                # We created a variable 'marks', which holds the value of 'readline()' method

    if not marks:                                       #
        break

    """
    The reason for 'if' condition being here instead of at the end is because if the same 'if' & 'break' statement
    were put in the end then after going over the 3rd and final line in the 'txt' file and printing line 33,34,35, in correspondence with the same
    It would have came back to 'marks = f.readline()' at line '9' and the variable 'marks' contains an empty string
    and would have given an error with 'm2 = marks.split(",")[1]' at line 24 because marks does not have any value to split and iterate at index [1]
    """

    i=i+1                                               # var 'i' is incremented by 1 everytime

    m1 = marks.split(",")[0]                            # var 'm1' holds the 'string' value at the zeroth index of the list returned by 'split()' method on 'marks'
    m2 = marks.split(",")[1]                            # var 'm2' holds the 'string' value at the first index of the list returned by 'split()' method on 'marks'
    m3 = marks.split(",")[2]                            # var 'm3' holds the 'string' value at the second index of the list returned by 'split()' method on 'marks'

    """
    IMPORTANT: The 'split()' method returns the substrings as lists and the comma (",") is the separator,
    So, 'marks = f.readline()' at line 9 reads all the lines inside the txt file one by one.
    Then, split() function with comma as separator divides and stores the line say '34,56,76' as [34,56,76] in a list format

    """


    print(f"The marks of student {i} in maths are {m1}")
    print(f"The marks of student {i} in sst are {m2}")
    print(f"The marks of student {i} in english are {m3}")


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# writelines() method:

""" The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple. """

# EXAMPLE:

# f = open('myfile.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()

"""
The above example code is commented out because otherwise we would have to create a separate file for the writelines() method,
The above code would have printed 4 lines with 'line 1','line 2','line 3' and a blank line because of the new-line character after 'line 3' in line 55
"""
