import pandas as pd
import glob
import os

count = 0

for file in glob.glob('/Users/patgardner/Desktop/tmp/popularity_export/*.csv'):
    split = (file.split('/')[-1]).split('.')
    if len(split) == 2:
        ticker = split[0]
    else:
        ticker = split[0] + '.' + split[1]
    df = pd.read_csv(file)
    if df.users_holding.iat[-1] < 2500:
        os.remove('/Users/patgardner/Desktop/tmp/popularity_export/' + ticker + '.csv')
        count += 1

print(count)
