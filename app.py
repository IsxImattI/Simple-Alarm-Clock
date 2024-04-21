import datetime
import time

print("ALARM CLOCK")

def alarm_clock():
    alarm_time = input("Enter the time for the alarm in the format HH:MM:SS: ")
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print("The current time is: ", current_time)
    while current_time != alarm_time:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("The current time is: ", current_time)
        time.sleep(1)
    print("ALARM!!!")

alarm_clock()