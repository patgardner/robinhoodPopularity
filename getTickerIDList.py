import glob
import urllib.request, json
import csv
import time

tickerPath = '/Users/patgardner/Desktop/tmp/popularity_export/*.csv'
with open('tickerIDs.csv', mode='w') as writeFile:
    writer = csv.writer(writeFile)
    for file in glob.glob(tickerPath):
        split = (file.split('/')[-1]).split('.')
        if len(split) == 2:
            ticker = split[0]
        else:
            ticker = split[0] + '.' + split[1]

        with urllib.request.urlopen('https://api.robinhood.com/instruments/?symbol=' + ticker) as url:
            try:
                id = (json.loads(url.read().decode()))['results'][0]['id']
                writer.writerow([ticker,id])
                time.sleep(0.5)
            except:
                continue
