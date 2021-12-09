from datetime import date, datetime

# The Spark Challenge Fall 2021
# Student Check-In Validation and Tracking
# Date Modified : 12/06/2021
# Import ECE Student PUID from verification file
# Import Matching Data From Records
# Track the number of visits
# Logs the transcript of visits

# Time Check
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")

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
            line = line.split('-')

            # Input verification check
            if(len(line) != 3):
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
            PUID = '' # Your while loop is running when PUID is empty --> Need to reset to prevent continuing to next part even though the swipe failed because it still produces something
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
            print("Check-Out Time :",datetime.now().strftime("%H:%M:%S"))
            print("Swipe Count : %d" % studentDB[PUID].count)
            
            # Add visit information to transcript log
            with open('checkout_logs.txt', 'a') as myFile:
                myFile.writelines(PUID+"-"+str(count)+"-"+datetime.now().strftime("%H:%M:%S")+'\n')
            with open('checkout_puid.txt', 'a') as myFile:
                myFile.writelines(PUID+'\n')
            with open('checkout_time.txt', 'a') as myFile:
                myFile.writelines(datetime.now().strftime("%H:%M:%S")+'\n')
            # Opening previous logs with PUID, num checkin, and time checkin
            with open('checkin_logs.txt', 'r') as logs:
                for line in logs.readlines():
                    # Finding check in time based on PUID
                    if (line.split('-')[0] == PUID):
                        # Write the time difference to file
                        with open('checkout_difference.txt', 'a') as myFile:
                            myFile.writelines(f'{PUID}-{str(datetime.strptime(datetime.now().strftime("%H:%M:%S"), "%H:%M:%S") - datetime.strptime(line.split("-")[2][:-2], "%H:%M:%S"))}\n')
                            print("Time Stayed : ", str(datetime.strptime(datetime.now().strftime("%H:%M:%S"), "%H:%M:%S") - datetime.strptime(line.split("-")[2][:-2], "%H:%M:%S")))
    # New Student visitor, verify ECE student and add to transcript
    else:
        if PUID in ECEStudents:
            studentDB[PUID] = student(PUID)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCheck-In Successful!")
            print("Check-In Time : ",datetime.now().strftime("%H:%M:%S"))
            print("Swipe Count : %d\n" % studentDB[PUID].count)
            with open('checkin_logs.txt', 'a') as myFile:
                myFile.writelines(PUID+"-"+"1"+"-"+datetime.now().strftime("%H:%M:%S")+'\n')
            with open('checkin_puid.txt', 'a') as myFile:
                myFile.writelines(PUID+'\n')
            with open('checkin_time.txt', 'a') as myFile:
                myFile.writelines(datetime.now().strftime("%H:%M:%S")+'\n')
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

