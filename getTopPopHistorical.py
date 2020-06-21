import pandas as pd
import glob
from operator import itemgetter

dates = ["2020-06-01","2020-06-02","2020-06-03","2020-06-04","2020-06-05","2020-06-08","2020-06-09","2020-06-10","2020-06-11","2020-06-12","2020-06-15","2020-06-16","2020-06-17","2020-06-18"]
path = "/Users/patgardner/Desktop/tmp/popularity_export/*.csv"

for date in dates:
    print(date)
    diffs = []
    for file in glob.glob(path):
        ticker = (file.split('/')[-1]).split('.')[0]
        oldQuant = 0
        newQuant = 0
        df = pd.read_csv(file)
        if df['timestamp'][0].split()[0] in dates:
            continue
        for i in df.index:
            if df['timestamp'][i].startswith(date):
                if oldQuant == 0:
                    oldQuant = df['users_holding'][i-1]
                tempHours = df['timestamp'][i].split()[1][0:2]
                if int(tempHours) > 13 and newQuant == 0:
                    newQuant = df['users_holding'][i]
                    diff = newQuant - oldQuant
                    diffs.append((ticker,diff,oldQuant,newQuant))
                    break
    # Sort list high to low - biggest diffs first
    diffs.sort(key=itemgetter(1), reverse=True)
    # Print top 15 increases in holdings
    for i in range(1,16):
        print(str(i) + ". " + diffs[i-1][0] + " " + str(diffs[i-1][1]) + " " + str(diffs[i-1][2]) + " " + str(diffs[i-1][3]))
