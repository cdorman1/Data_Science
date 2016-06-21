import time
from dateutil.parser import parse
import collections
import pandas as pd
import sqlite3 as lite
import matplotlib.pyplot as plt
import requests
import datetime

con = lite.connect('weather.db')
cur = con.cursor()

cities = {"Atlanta": '33.762909,-84.422675',
          "Austin": '30.303936,-97.754355',
          "Boston": '42.331960,-71.020173',
          "Chicago": '41.837551,-87.681844',
          "Cleveland": '41.478462,-81.679435'
          }

for city in cities:
    LL = cities[city].split(',')
    LATITUDE = LL[0]
    LONGITUDE = LL[1]
#
#     r = requests.get('http://www.citibikenyc.com/stations/json')
#     exec_time = parse(r.json()['executionTime']).strftime("%s")
#
#     cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time,))
#
#     for station in r.json()['stationBeanList']:
#         cur.execute("UPDATE available_bikes SET _%d = %d WHERE execution_time = %s" % (station['id'], station['availableBikes'], exec_time))
#     con.commit()
#
#
# con.close() #close the database connection when done

start_date = datetime.datetime.now() - datetime.timedelta(days=30)
end_date = datetime.datetime.now()
days = datetime.timedelta(days=1)
while start_date <= end_date:
    start_date = start_date + days
    utc = start_date.strftime('%s')
    r = requests.get('https://api.forecast.io/forecast/c2b68277c04676d8a548d062ce395ccf/{0},{1},{2}'.format(LATITUDE, LONGITUDE, utc ))
    data = r.json()
    print start_date, data['daily']['data'][0]['temperatureMax']




