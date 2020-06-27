import pandas as pd
import glob
from operator import itemgetter
import csv

oldHash = dict()
newHash = dict()

with open('stocksPopNight.csv', mode='r') as readFile:
    csvFile = csv.reader(readFile)
    for lines in csvFile:
        oldHash[lines[0]] = lines[1]

with open('stocksPopCurrent.csv', mode='r') as readFile:
    csvFile = csv.reader(readFile)
    for lines in csvFile:
        newHash[lines[0]] = lines[1]

diffs = []

for key in oldHash:
    try:
        oldQuant = int(oldHash[key])
        newQuant = int(newHash[key])
        diff = newQuant - oldQuant
        diffs.append((key,diff,oldQuant,newQuant))
    except:
        print("Error in a diff.")

# Sort list high to low - biggest diffs first
diffs.sort(key=itemgetter(1), reverse=True)

# Print top 15 increases in holdings
for i in range(1,16):
    print(str(i) + ". " + diffs[i-1][0] + " " + str(diffs[i-1][1]) + " " + str(diffs[i-1][2]) + " " + str(diffs[i-1][3]))
