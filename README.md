# The Spark Challenge Student Check-In/Out Tracking Script
This Python Script uses the Student ID Database to match the entries with the ID Card Swipe and records the entries and swipe times.
>Big thanks to Claire Poukey!!

>The verification file is not included in this repository since
>it includes sensitive and confidential information about students

>Example Test String : `;000000000=2229=0012372676=02?`

>You have to create a text file `verification.txt` with the string `0012372676`

What Do You Need To Run This Script?
==============
* Python3
* ID Number Database (verification.txt)
* Magnetic Card Strip Reader

How to Run This Script?
==========
1.  Clone the script to your machine
2.  Connect the magnetic card strip reader to your machine
3.  Run the command `make check-in` in terminal
4.  Swipe card once for check-in
5.  Swipe card second time for check-out
6.  When you are done with all entries exit the program safely using `exit` command when `SWIPE PUID` prompted.
7.  Run the attandance script by running the command `make attendance`
>Note that the script stops recording after 2 swipes and the entries need to be deleted manually from the log file.

What This Script Does?:
------------------------
1. Records the check-in time with the first card swipe
2. Records the check-out time with the second card swipes
3. Ignores the entries after second card swipe
4. Takes the difference between the check-in and check-out time to see how long the student stayed at the event
5. Prints the ID card number and the time stayed to a CSV File


Parts of This Script:
==========
1. Python Script (checkin.py)
2. Attendance Script (attandance.py)
3. Makefile (to make things a little easier)
4. Log Files

Things to be Careful About:
==========
1. Running `make clean` clears the log files so use with caution
2. If the program crashes for some reason you have to manually rerun the script using *make check-in* command
3. You have to manually run `make attendance` after the event is over to process the data.


Things That Still Need Attention:
------------------------
1. Nothing. (To be updated)

