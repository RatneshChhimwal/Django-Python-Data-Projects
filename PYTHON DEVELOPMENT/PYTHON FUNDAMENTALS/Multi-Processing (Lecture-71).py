# MULTI_PROCESSING

import requests                                                                                 # We import 'requests' module
import multiprocessing                                                                          # We import 'multiprocessing' module

def downloadFile(url, name):                                                                    # We created a function 'downloadFile' with 'url' & 'name' as argument
    print(f"Started Downloading {name}")                                                        # Printing f-string
    response = requests.get(url)                                                                # We make the request call using 'get' function with url as argument and assign the results to variable 'response'
    (open(f"C:\\Users\\ratne\\Desktop\\DownloadedMulti-Processing\\file{name}.jpg", "wb")       # We store and 'open' the downloaded file in 'wb' mode (write-binary)
     .write(response.content))                                                                  # We use the 'write' function with 'response.content'
    print(f"Finished Downloading {name}")                                                       # Printing f-string

def main():                                                                                     # We create a 'main' function storing the url for file download
    url = "https://picsum.photos/2000/3000"


    # Download using multiprocessing

    pros = []                                                                                   # We create a list 'pros' to store all the processes to later 'join'
    for i in range(50):                                                                         # We create a 'for' loop for the value of 'i'
        p = multiprocessing.Process(target=downloadFile, args=(url, i))

        # We use the 'Process' method from the class 'multiprocessing' with the function to be executed as 'target' and arguments as 'args' and assign the results to variable 'p'

        p.start()                                                                               # We start the process with 'p.start()'
        pros.append(p)                                                                          # We append each result of process 'p' to the list 'pros'

    for p in pros:                                                                              # We start a 'for' loop to iterate through the list 'pros'
        p.join()                                                                                # We use the keyword 'join()' with each iteration of value 'p'

    print("All downloads completed.")                                                           # Printing 'string'

if __name__ == "__main__":                                                                      # Refer to 'Lecture-33'
    main()                                                                                      # This idiom is necessary to ensure that the 'main' function is not automatically executed if the script is imported
