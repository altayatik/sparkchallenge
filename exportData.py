import csv

puids = []
visitLens = []

# Get the puids and visit lengths
with open('checkout_difference.txt', 'r') as f:
    for line in f.readlines():
        line = line.split('-')
        puids.append(line[0])
        visitLens.append(line[1][:-1])

# Zips into csv with column formatting
with open('attendance.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(zip(puids, visitLens))
