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
VISITATION_LOG_FILE = 'checkout_logs.txt'


# Data Structures
class student:
    def __init__(self, puid):
        self.puid = puid
        self.count = 1

#Import Student ID's from verification file

def initialize():
    print('Reading the Database...')

    # Load ECE student IDs from file
    with open(STUDENT_ID_FILE, 'r') as myFile:
        for line in myFile.readlines():
            ECEStudents.append(line.strip())

    print('Validating visit history...')
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
        if studentDB[PUID].count >= 2:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n!!!Already Checked-Out!!!\n")
            print("Swipe Count More Than %d\n" % studentDB[PUID].count)
        else:
            studentDB[PUID].count += 1
            count = studentDB[PUID].count
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCheck-Out Successful!")
            print("Check-Out Time :",current_time)
            print("Swipe Count: %d\n" % studentDB[PUID].count)
            # Add visit information to transcript log
            with open('checkout_logs.txt', 'a') as myFile:
                myFile.writelines(PUID+":"+str(count)+":"+current_time+'\n')
    # New Student visitor, verify ECE student and add to transcript
    else:
        if PUID in ECEStudents:
            studentDB[PUID] = student(PUID)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCheck-In Successful!")
            print("Check-In Time :",current_time)
            print("Swipe Count: %d\n" % studentDB[PUID].count)
            with open('checkin_logs.txt', 'a') as myFile:
                myFile.writelines(PUID+":"+"1"+":"+current_time+'\n')
        else:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n!!!NOT AN ECE STUDENT!!!")

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




