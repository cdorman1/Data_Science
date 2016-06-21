import time
from dateutil.parser import parse
import collections
import sqlite3 as lite
import pandas as pd
import sqlite3 as lite
import matplotlib.pyplot as plt
import requests
import datetime

API_KEY = 'c2b68277c04676d8a548d062ce395ccf'

url = 'https://api.forecast.io/forecast/' + API_KEY + '/'

cities = { "Atlanta": '33.762909,-84.422675',
            "Austin": '30.303936,-97.754355',
            "Boston": '42.331960,-71.020173',
            "Chicago": '41.837551,-87.681844',
            "Cleveland": '41.478462,-81.679435'
        }

end_date = datetime.datetime.now()

con = lite.connect('weather.db')
cur = con.cursor()

# with con:
#     cur.execute('CREATE TABLE IF NOT EXISTS daily_temp ( day_of_reading INT,  "Atlanta" REAL, "Austin" REAL, "Boston" REAL, "Chicago" REAL, "Cleveland" REAL);')
#
# query_date = end_date - datetime.timedelta(days=30)
#
# with con:
#     while query_date < end_date:
#         cur.execute("REPLACE INTO daily_temp(day_of_reading) VALUES (?)", (int(query_date.strftime('%s')),))
#         query_date += datetime.timedelta(days=1)
#
#
# for k, v in cities.iteritems():
#     v = v.split(',')
#     latitude = v[0]
#     longitude = v[1]
#     query_date = end_date - datetime.timedelta(days=30)
#     while query_date < end_date:
#         r = requests.get(url + latitude + ',' + longitude + ',' + query_date.strftime('%Y-%m-%dT12:00:00'))
#
#         with con:
#             cur.execute('UPDATE daily_temp SET ' + k + ' = ' + str(r.json()['daily']['data'][0]['temperatureMax']) + ' WHERE day_of_reading = ' + query_date.strftime('%s'))
#
#         query_date += datetime.timedelta(days=1)

df = pd.read_sql_query('SELECT * FROM daily_temp;', con)
df.day_of_reading = pd.to_datetime(df['day_of_reading'], unit='s')

hour_change = collections.defaultdict(int)
for col in df.columns:
    if col == 'day_of_reading':
        continue
    temp_vals = df[col].tolist()
    key = col
    temp_change = 0
    for k, v in enumerate(temp_vals):
        print key, k, v
#     hour_change[key] = temp_change #convert the station id back to integer
#
# print hour_change
con.close()
