"""

Write a program to pronounce list of names using win32 API. If you are given a list l as follows:

l = ["Rahul", "Nishant", "Harry"]

Your program should pronounce:

Shoutout to Rahul
Shoutout to Nishant
Shoutout to Harry

"""

import win32com.client                                  # We imported the win32com.client module, which provides access to the Windows COM (Component Object Model) API. COM allowing communication between different software components on Windows.

speaker = win32com.client.Dispatch("SAPI.SpVoice")      #  We created an instance 'speaker' of the COM object named "SAPI.SpVoice" using the Dispatch method. "SAPI.SpVoice" is a Speech API (SAPI) object that allows for text-to-speech synthesis.

l = ["Rahul", "Nishant", "Harry"]                       # We created the list 'l'

for i in l:                                             # We created a loop to iterate over the list 'l'
    text = f"Shoutout to {i}"                           # We created a variable 'text' and assigned it an f-string
    speaker.Speak(text)                                 # We used the 'speak' method upon the 'Speaker' object with 'text' as an argument