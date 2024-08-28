"""

Write a python program which reminds you of drinking water every hour or two.
Your program can either beep or send desktop notifications for a specific operating system

"""


import time                                                             # We imported 'time' module
import win32com.client                                                  # We imported win32com.client module
from datetime import datetime, timedelta                                # We imported the datetime module

def notification():                                                     # We defined a function 'notification()'

    # Set the initial value for two_hour_gap

    two_hour_gap = datetime.now() + timedelta(hours=2)                  # We created a variable 'two_hour_gap', which holds the value of time 2 hours after the real-time

    while True:                                                         # We start a while-loop, Which has the variable 'current_time' inside it

        current_time = datetime.now()

        # IMPORTANT: The reason we started a 'while' loop is because we want to continuously run it and update the value of 'current_time', So that the following 'if' condition can be true some-time after almost 2 hours

        if current_time >= two_hour_gap:                                # We start an 'if' loop to check the condition if the current_time is greater than or equal to two_hour_gap
            speaker = win32com.client.Dispatch("SAPI.SpVoice")          # Once the 'if' condition is true, We define a variable 'speaker' which holds the instance of the class SAPI.SpVoice
            text = "Kindly drink water"                                 # We define the string and assign it to a variable 'text'
            speaker.Speak(text)                                         # We use the 'Speak' method of the 'speaker' object and pass 'text' as argument

            # Update two_hour_gap for the next occurrence
            # To ensure that the loop is not continuously executed once the current_time passes the previous value of 'two_hour_gap'

            two_hour_gap = current_time + timedelta(hours=2)            # We update the value of 'two_hour_gap' for 2 hours further after the execution of 'if' condition

        # Introduce a delay (e.g., 1 minute) to avoid continuous looping

        time.sleep(60)                                                  # We use time.sleep(60) to ensure that the while loop is not executed continuously, We halt the execution for a minute

# Call the notification function

notification()


# IMPORTANT: -----------------------------------------------------------------------------------------------------------

"""


The provided program lacks efficiency in memory utilization, particularly in scenarios where periodic execution,
like every minute on a server, is involved. The continuous execution of the 'while True' loop for repeated update of current_time,
leads to constant resource consumption.
A more optimal approach would involve utilizing a scheduling mechanism or task scheduler
to trigger the notification function at specific intervals, ensuring the program runs only when needed.
This reduces the need for continuous looping and enhances memory efficiency, making it more suitable for server environments
where resource allocation is a critical consideration.

"""



