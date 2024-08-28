"""

Write a program to clear the clutter inside a folder on your computer.
You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder.
Do the same for other file formats. For example:

sfdsf.png --> 1.png
vfsf.png --> 2.png
this.png --> 3.png
design.png --> 4.png
name.png --> 5.png

"""

import os

Folder_Path = r"C:\Users\ratne\AppData\Roaming\JetBrains\PyCharmCE2023.2\scratches\Use Exercise OS-rename"

"""
The 'r' stands for "raw," and it indicates that backslashes \ within the string
should be treated as literal characters rather than as escape characters.
"""

for i,filename in enumerate(os.listdir(Folder_Path), start=0):      # We used a 'for' loop with 'enumerate' function to go through the files inside the directory/folder
    if filename.endswith('.png'):                                   # 'if' condition for when the value of the variable 'filename' ends with '.png'
        i+=1                                                        # Incrementing the value of index holder 'i' with '1' everytime the 'if' condition is satisfied
        old_path = os.path.join(Folder_Path, filename)              # We defined a variable 'old_path' that uses 'os.path.join' function to concatenate the folder_path and filename into a complete file path
        new_filename = str(i)+'.png'                                # We define a new variable 'new_filename' that holds the new name as string of 'i' concatenated with '.png' for file extension
        new_path = os.path.join(Folder_Path, new_filename)          # We define a variable 'new_path' that joins the file path for the directory with 'new_filename'
        os.rename(old_path, new_path)                               # os.rename

print("Files renamed successfully")
