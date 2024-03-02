# The Spark Challenge Student Check-In/Out Tracking Script
[![license](https://img.shields.io/badge/license-APGL--3.0-brightgreen?style=flat-square)](https://github.com/altayatik/sparkchallenge/blob/main/LICENSE)  
This Python Script uses the Student ID Database to match the entries with the ID Card Swipe and records the entries and swipe times.

>The verification file is not included in this repository since
>it includes sensitive and confidential information about students

>Example Test String : `==0012372676`

>You have to create a plain text file `verification.txt` with the string `0012372676`

What Do You Need To Run This Script?
==============
* Python3
* ID Number Database (verification.txt)
* Magnetic Card Strip Reader / Pinpad

How to Run This Script?
==========
macOS/Linux:
------------------------
1.  Clone the script to your machine
2.  Connect the magnetic card strip reader or pinpad to your machine
3.  Run the command `make check-in` in terminal
4.  Swipe card or enter id with "==" at the beginning once for check-in
5.  Swipe card enter id with "==" second time for check-out
6.  When you are done with all entries exit the program safely using `exit` command when `SWIPE PUID` prompted.
7.  Run the attandance script by running the command `make attendance`

Windows:
------------------------
1.  Clone the script to your machine
2.  Connect the magnetic card strip reader or pinpad to your machine
3.  Run the command `python3 checkin.py` in terminal
4.  Swipe card or enter id with "==" at the beginning once for check-in
5.  Swipe card enter id with "==" second time for check-out
6.  When you are done with all entries exit the program by halting the process withn `CTRL+C` command when `SWIPE PUID` prompted.
7.  Run the attandance script by running the command `python3 exportData.py`


>Note that the script stops recording after 2 swipes and the entries need to be deleted manually from the log file.

What Does This Script Do?:
------------------------
1. Records the check-in time with the first card swipe/entry
2. Records the check-out time with the second card swipes/entry
3. Ignores the entries after second card swipe/entry
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
1. Running `make clean` clears the log files so use with caution. (Does not work in Windows)
2. If the program crashes for some reason you have to manually rerun the script using `make check-in` or `python3 checkin.py` depending on the OS.
3. You have to manually run `make attendance` or `python3 exportData.py` depending on OS after the event is over to process the data.


Things That Still Need Attention:
------------------------
1. The contents of `verification.txt` must be plain text or the script won't run correctly
2. Makefile does not work in Windows machines; `todo:` create an executable for windows.

Trivia
------------------------
The Spark Challenge is a student-led undergraduate project competiton hosted by Purdue University's School of Electrical and Computer Engineering. This script was developed by Altay Atik (The Spark Challenge Moderator at the time 2019-2022), with valuable contributions of Claire Poukey and Vivek Panchagnula (Spark Challenege Committee Members at the time 2019-2022). The contents of this program is not affiliated or belong to Purdue Univesity or any of it's subsidiaries, all rights belong to and reserved to the students contributed to the development and subject to copyright laws. For more information see below.


License
------------------------
This script is protected by GNU Affero General Public License v3.0. and The Copyright Law of the United States (Title 17). For details and legal information visit LICENSE.

