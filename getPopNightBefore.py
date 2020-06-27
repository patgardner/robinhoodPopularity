import glob
import urllib.request, json
import csv
import time

with open('stocksPopNight.csv', mode='w') as writeFile:
    with open('tickerIDs.csv', mode='r') as readFile:
        writer = csv.writer(writeFile)
        csvFile = csv.reader(readFile)
        for cols in csvFile:
            with urllib.request.urlopen('https://api.robinhood.com/instruments/' + cols[1] + '/popularity/') as url:
                num = (json.loads(url.read().decode()))['num_open_positions']
            writer.writerow([cols[0],num])
            time.sleep(0.9)
