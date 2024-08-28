"""

Write a Library class with no_of_books and books as two instance variables.
Write a program to create a library from this Library class and show how you can print all books,
add a book and get the number of books using different methods.
Show that your program doesn't persist the books after the program is stopped!

"""

#Books is a list
#No_of_books is an integer

class Library():                                # We created a class 'Library'
    def __init__(self):                         # Constructor for class 'Library' no arguments as we do not want any input number of books or a book name from the user
        self.no_of_books=0                      # We assigned a static value for attribute/instance variable 'no_of_books' as '0' to begin with
        self.books_stored=[]                    # We assigned an empty list [] to attribute books_stored to store name of the books later on

    def display_books(self):                    # 'display_books' function to display the names of all the books stored in list 'books_stored'
        if self.no_of_books==0:                 # 'if' condition for when the list is empty
            print(f"The list is empty")         # Printing string 'The list is empty'
        else:
            for i in self.books_stored:         # 'for' loop inside the else condition to iterate through the elements of the list 'books_stored' one by one
                print(i)                        # Printing the names of the books

    def add_book(self,book):                    # 'add_book' function to add a new book in the list 'books_stored' with argument 'book'
        self.books_stored.append(book)          # We append the string value from 'book' argument to the list 'books_stored'
        self.no_of_books+=1                     # & also increment the attribute 'no_of_books' with '1'

    def get_no_of_books(self):                  # 'get_no_of_books' to display the number of books
        print(self.no_of_books)                 # Prints the attribute 'self.no_of_books'
        return


My_Library=Library()                            # Creating an object 'My_Library' from class 'Library()'

My_Library.add_book("Hindi")                    # Calling the 'add_book' function on object 'My_Library' with "Hindi" as the value for argument 'book'
My_Library.add_book("English")                  # Calling the 'add_book' function on object 'My_Library' with "English" as the value for argument 'book'
My_Library.add_book("Math")                     # Calling the 'add_book' function on object 'My_Library' with "Math" as the value for argument 'book'

My_Library.display_books()                      # Calling the 'display_books' function on object 'My_Library'

My_Library.get_no_of_books()                    # Calling the 'get_no_of_books' function on object 'My_Library'