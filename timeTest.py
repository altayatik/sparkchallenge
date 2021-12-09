from datetime import datetime

PUID = '########'
count = 1
timeFormat = '%H:%M:%S'

checkin = f'{PUID}-{count}-20:22:02'

count += 1
checkout = f'{PUID}-{count}-{str(datetime.now().strftime(timeFormat))}'

print(f'Checkin Log: {checkin}\nCheckout Log: {checkout}\n')

# Get only the time from the log
checkinTime = checkin.split('-')[2]
checkoutTime = checkout.split('-')[2]

# Update to datetime object type to allow for time algebra
checkinTime = datetime.strptime(checkinTime, timeFormat)
checkoutTime = datetime.strptime(checkoutTime, timeFormat)

print(f'Checkin Time: {checkinTime}\nCheckout Time: {checkoutTime}\n')

# Calculate difference between checkout time and check in time
diff = checkoutTime - checkinTime
print(f'Difference: {diff}')

