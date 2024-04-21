Alarm Clock Script
This Python script serves as a simple alarm clock that allows you to set an alarm for a specific time. When the time matches the set alarm time, the script will alert you by printing "ALARM!!!" to the console.

Features
Simple User Interface: The alarm time is set via a command-line prompt.
Real-Time Feedback: Continuously displays the current time and updates it every second until the alarm time is reached.
Exact Time Match: The alarm triggers exactly when the system clock matches the set time.

Requirements
To run this script, you need Python installed on your system. The script is compatible with Python 3.x and uses the following built-in libraries:

datetime: For handling time operations.
time: For creating delay to simulate real-time clock updates.

How to Run the Script:
Make sure Python is installed on your system.
Download the script to your local machine.
Open your command line interface (CLI).
Navigate to the directory where the script is located.
Run the script using the command:
python alarm_clock.py
Follow the on-screen prompts to set the alarm time in the format HH:MM:SS (e.g., 13:45:00 for 1:45 PM).

Limitations
The script must remain running and cannot be minimized or closed; otherwise, the alarm will not function.
It operates based on the system clock and assumes the system time is correctly set.
The script does not include sound; it only displays a text alert.
