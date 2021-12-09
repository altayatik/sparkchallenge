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
# current_time = now.strftime(TIME_FORMAT)

# Visit Limit
COUNT_LIMIT = 1

# Import verification
STUDENT_ID_FILE = 'verification.txt'

# Visit Logs
VISITATION_LOG_FILE = 'checkout_logs.txt'

# datetime standard format
TIME_FORMAT = '%H:%M:%S'


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
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n!!!Already Checked-Out!!!\n')
            print(f'Swipe Count More Than {studentDB[PUID].count}\n')
        else:
            studentDB[PUID].count += 1
            count = studentDB[PUID].count
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCheck-Out Successful!')
            print(f'Swipe Count: {studentDB[PUID].count}')

            checkoutTime = datetime.now().strftime(TIME_FORMAT)
            print(f'\nCheckout Time: {checkoutTime}')
            
            # Converts to datetime object
            checkoutTime = datetime.strptime(checkoutTime, TIME_FORMAT)
            
            # Add visit information to transcript log
            with open('checkout_logs.txt', 'a') as myFile:
                myFile.writelines(f'{PUID}-{count}-{datetime.now().strftime(TIME_FORMAT)}\n')

            with open('checkout_puid.txt', 'a') as myFile:
                myFile.writelines(f'{PUID}\n')

            with open('checkout_time.txt', 'a') as myFile:
                myFile.writelines(f'{checkoutTime}\n')

            # Opening previous logs with PUID, num checkin, and time checkin
            with open('checkin_logs.txt', 'r') as logs:
                for line in logs.readlines():
                    # Finding check in time based on PUID
                    if (line.split('-')[0] == PUID):
                        checkinTime = line.split('-')[2][:-2] # The [:-2] ignores the last two characters "\n"
                        print(f'Checkin Time: {checkinTime}')

                        # Converts to datetime object
                        checkinTime = datetime.strptime(checkinTime, TIME_FORMAT)

                        # Calculates difference between checkout time and check in time
                        diff = checkoutTime - checkinTime
                        print(f'Time Stayed: {diff}')

                        # Write the time difference to file
                        with open('checkout_difference.txt', 'a') as myFile:
                            myFile.writelines(f'{PUID}-{str(diff)}\n')
    # New Student visitor, verify ECE student and add to transcript
    else:
        if PUID in ECEStudents:
            checkinTime = datetime.now().strftime(TIME_FORMAT)
            studentDB[PUID] = student(PUID)

            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCheck-In Successful!')
            print(f'Check-In Time : {checkinTime}')
            print(f'Swipe Count : {studentDB[PUID].count}\n')

            with open('checkin_logs.txt', 'a') as myFile:
                myFile.writelines(f'{PUID}-1-{checkinTime}\n')

            with open('checkin_puid.txt', 'a') as myFile:
                myFile.writelines(f'{PUID}\n')

            with open('checkin_time.txt', 'a') as myFile:
                myFile.writelines(f'{checkinTime}\n')
        else:
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n!!!NOT AN ECE STUDENT!!!')

if __name__ == "__main__":
    # Establish Data Structures
    studentDB = {}
    ECEStudents = []

    # Initialize
    print('Spark Check-In Script Initalizing')
    initialize()

    print('System initialized successfully. Type exit to halt program safely.\n\n')
    # Begin program
    while(True):
        response = verfifyStudent()
