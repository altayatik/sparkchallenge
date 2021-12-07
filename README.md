# The Spark Challenge Student Check-In/Out Tracking Script
This Python Script uses the Student ID Database to match the entries with the ID Card Swipe and records the entries and swipe times.

>The verification file is not included in this repository since
>it includes sensitive and confidential information about students

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
>Note that the script stops recording after 2 swipes and the entries need to be deleted manually from the log file.

Parts of This Script:
==========
1. Python Script (checkin.py)
2. Makefile (to make things a little easier)
3. Log Files

Things to be Careful About:
==========
1. Running `make clean` wipes the log files so use with caution
2. If you run `make clean` you have to manually create *checkin_logs.txt* and *checkout_logs.txt*
3. 


Things That Still Need Attention:
------------------------
1. If the script crashes for some reason you have to re-run the script manually to keep recording

