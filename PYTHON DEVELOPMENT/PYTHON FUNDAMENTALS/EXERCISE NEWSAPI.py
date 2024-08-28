# IMPORTANT: ***********************************************************************************************************

"""

Use the NewsAPI and the request module to fetch the daily news related to different topics.
Go to: https://newsapi.org/ and explore the various options to build your application

"""

import requests                                                                 # We imported the 'request' module/library
import bs4                                                                      # We imported the 'bs4' library used for web scraping (process of automatically extracting information or data from websites).
from bs4 import BeautifulSoup                                                   # We imported the 'BeautifulSoup' module used for parsing HTML and XML documents, making it easy to extract and navigate the data during web scraping.

url = ("https://newsapi.org/v2/top-headlines?country=in&category"               # We created a variable 'url' which holds the URL for API call to the 'newsapi' service
       "=general&language=hi&pageSize=10&page=1&apiKey=170965ab0c634dc3816798a62c355e62")

getcall = requests.get(url)                                                     # We use the 'requests.get(url)' method to make the 'get' request to the 'newsapi' server

# print(getcall.text)                                                           # We can print the data fetched and stored inside 'getcall' as text

soup = BeautifulSoup(getcall.text, 'html.parser')                       # We created an object 'soup' from the class 'BeautifulSoup' with 'getcall.text' and 'html.parser' as arguments

# print(soup.prettify())                                                        # We can print the parsed html data stored inside object 'soup' while using the 'prettify' method (used to improve the readability of the HTML or XML content)

"""

For HTTP response, the 'status_code' is a part of the response that indicates the status of the request.
A status code of 200 specifically refers to a successful HTTP request.

Mentioned below are few other status codes: ---

200 OK: The request was successful, and the server returned the requested data.

201 Created: The request was successful, and a new resource was created as a result.

204 No Content: The server successfully processed the request but there is no content to send back.

400 Bad Request: The request could not be understood or was missing required parameters.

404 Not Found: The requested resource could not be found on the server.

"""

if getcall.status_code==200:                                                    # We start an 'if-else' loop, firstly checking if getcall.status_code==200 (OK)
    data=getcall.json()                                                         # We create a variable 'data' and assign it a 'json' of the data fetched by 'getcall'

"""
List comprehension is a concise way to create lists in Python. It consists of an expression followed by a for loop inside square brackets.
Below commented is the syntax for List comprehension:
"""

# new_list = [expression for item in iterable if condition]                     # SYNTAX: LIST COMPREHENSION

titles = [article['title'] for article in data['articles']]

a = int(input("Choose a number from the below:\n"
              "1:business\n2:entertainment\n3:general-health\n4:science\n5:sports\n6:technology\n"))        # We created a variable 'a' to store the user input


category = {1: "business", 2: "entertainment", 3: "general-health", 4 :"science", 5: "sports", 6: "technology"}     # We created a dictionary 'category' to map the news category with corresponding integer

if a in category:
    getcallcategory = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category={category[a]}&langauge=hi"        # We make the 'get' request to the 'newsapi' server and store the data received inside 'getcallcategory'
                                   f"&pageSize=10&page=1&apiKey=170965ab0c634dc3816798a62c355e62")

    if getcallcategory.status_code == 200:                                                      # We check for successful status_code (200)
        data_category = getcallcategory.json()                                                  # We store the data received in a JSON format inside 'data_category'
        titles_category = [article['title'] for article in data_category['articles']]           # List comprehension to fetch the 'titles' from the article
        for headlines in titles_category:                                                       # Iterating through the list 'titles_category'
            print(headlines)
    else:                                                                                       # 'else' condition for 'getcallcategory' request fail
        print(f"Error fetching news for category {category[a]}")
else:                                                                                           # 'else' condition for if the user input does not exist in dictionary 'category'
    print("Invalid choice. Please choose a number from 1 to 6.")