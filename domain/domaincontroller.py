from Rider import Rider
import csv
import numpy as np

file = open('rider.csv', newline='')
csvreader = csv.reader(file)
list = list(csvreader)

rows = []

for item in list:
    for i in item:
        rows.append(i.split(';'))


print(rows)




for row in rows:
    
    rider = Rider(row[1], row[0], row[2])
    
    print(rider.name, rider.team, rider.value, rider.general_points, rider.mountain_points, rider.sprint_points)
    print("\n")


