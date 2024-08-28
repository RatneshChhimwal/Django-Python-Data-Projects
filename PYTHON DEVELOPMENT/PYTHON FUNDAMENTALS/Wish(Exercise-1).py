# create a program capable of wishing good morning, evening, night, using time module to get the current hour

import datetime

current_time=datetime.datetime.now()
print(current_time)

hour1=current_time.hour
print(hour1)

match hour1:
    case _ if 24<hour1<12:
        print("good morning")
    case _ if 12<hour1<18:
        print("good evening")
    case _ if 18<hour1<24:
        print("good night")


# Now the same thing but with if-elif-else:

current_time1=datetime.datetime.now()
print(current_time1)

hour2=current_time.hour
print(hour2)

if 0<hour2<=12:
    print("good morning")
elif 12<=hour2<=18:
    print("good evening")
else:
    print("good night")