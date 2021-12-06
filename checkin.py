from datetime import datetime

# The Spark Challenge Fall 2021
# Student Check-In Validation and Tracking
# Date Modified : 12/06/2021
# Import ECE Student PUID from verification file
# Import Matching Data From Records
# Track the number of visits
# Logs the transcript of visits

# Time Check
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# Visit Limit
COUNT_LIMIT = 1

# Import verification
STUDENT_ID_FILE = 'verification.txt'

# Visit Logs
VISITATION_LOG_FILE = 'checkin_logs.txt'


# Data Structures
class student:
    def __init__(self, puid):
        self.puid = puid
        self.count = 1

#Import Student ID's from verification file

def initialize():
    print('Populating ECE student data from verification.txt ...')

    # Load ECE student IDs from file
    with open(STUDENT_ID_FILE, 'r') as myFile:
        for line in myFile.readlines():
            ECEStudents.append(line.strip())

    print('Populating student visit history from ECESnackTime.txt ...')
    # Load visit transcript file - populate student dictionary
    with open(VISITATION_LOG_FILE, 'r') as myFile:
        for line in myFile.readlines():
            line = line.split(':')

            # Input verification check
            if(len(line) != 2):
                print('ERROR READING IN STUDENT HISTORY DATABASE')
                return

            #Extract information from line
            [PUID, count] = line

            if PUID in studentDB.keys():
                # Student previously added - UPDATE COUNT
                if int(count) > studentDB[PUID].count:
                    studentDB[PUID].count = int(count)
            else:
                # New Student, add to dictionary
                newstudent = student(PUID.strip())
                studentDB[PUID.strip()] = newstudent
                studentDB[PUID].count = int(count)

    print(studentDB.keys);

def verfifyStudent():
    PUID = ''
    count = 0

    # Get PUID Number from scanner
    while PUID == '':
        PUID = input('Swipe PUID...')
        PUID = PUID.strip()
        PUID = PUID.split('=')
        try:
            PUID = PUID[2]
        except IndexError:
            print('ERROR READING CARD')
        PUID = PUID[1:]
        if PUID == 'exit':
            print('Exit Success')
            exit(0)
    print(studentDB.keys())
    # Check if student has visited before
    if PUID in studentDB.keys():
        # Verify visit is valid
        if studentDB[PUID].count >= 1:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCheck-Out Successful!\n")
            print("Check-Out Time",current_time)
            with open('checkout_logs.txt', 'a') as myFile:
                myFile.writelines(PUID+":"+current_time+'\n')
        else:
            studentDB[PUID].count += 1
            count = studentDB[PUID].count
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCheck-In Successful")
            print("Check-In Time",current_time)
            # Add visit information to transcript log
            with open('checkin_time.txt', 'a') as myFile:
                myFile.writelines(PUID+":"+current_time+'\n')
    # New Student visitor, verify ECE student and add to transcript
    else:
        if PUID in ECEStudents:
            studentDB[PUID] = student(PUID)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCheck-In Successful")
            print("Check-In Time",current_time)
            with open('checkin_logs.txt', 'a') as myFile:
                myFile.writelines(PUID+":"+current_time+'\n')
        else:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNOT AN ECE STUDENT USE QR CODE")



if __name__ == "__main__":
    # Establish Data Structures
    studentDB = {}
    ECEStudents = []

    # Initialize
    print('Spark Check-In Script Initalizing')
    initialize()

    print("System initialized successfully. Type exit to halt program safely.\n\n")
    # Begin program
    while(True):
        response = verfifyStudent()




