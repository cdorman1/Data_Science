import pandas as pd
import sqlite3 as lite

# Create tuple of tuples containing information to insert in DB
cities = (('New York City', 'NY'),
          ('Boston', 'MA'),
          ('Chicago', 'IL'),
          ('Miami', 'FL'),
          ('Dallas', 'TX'),
          ('Seattle', 'WA'),
          ('Portland', 'OR'),
          ('San Francisco', 'CA'),
          ('Los Angeles', 'CA'),
          ('Washington', 'DC'),
          ('Houston', 'TX'),
          ('Las Vegas', 'NV'),
          ('Atlanta', 'GA'))

weather = (('New York City', 2013, 'July', 'January', 62),
           ('Boston', 2013, 'July', 'January', 59),
           ('Chicago', 2013, 'July', 'January', 59),
           ('Miami', 2013, 'August', 'January', 84),
           ('Dallas', 2013, 'July', 'January', 77),
           ('Seattle', 2013, 'July', 'January', 61),
           ('Portland', 2013, 'July', 'December', 63),
           ('San Francisco', 2013, 'September', 'December', 64),
           ('Los Angeles', 2013, 'September', 'December', 75),
           ('Houston', 2013, 'July', 'January', 78),
           ('Washington', 2013, 'July', 'January', 62),
           ('Las Vegas', 2013, 'July', 'December', 82),
           ('Atlanta', 2013, 'July', 'January', 68))

con = lite.connect('getting_started.db')

# Inserting rows by passing tuples to `execute()`
with con:

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS cities")
    cur.execute("DROP TABLE IF EXISTS weather")
    cur.execute("CREATE TABLE cities (name text, state text)")
    cur.execute("CREATE TABLE weather (city text, year integer, warm_month text,"
                " cold_month text, average_high integer)")
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
    data = cur.execute("SELECT city, state"
                       " FROM cities INNER JOIN weather ON name = city"
                       " WHERE warm_month = 'July' ORDER BY average_high DESC")

    rows = data.fetchall()
    cols = [desc[0] for desc in data.description]
    df = pd.DataFrame(rows, columns=cols)
    df_cities = df['city'].tolist()
    df_states = df['state'].tolist()
    df = zip(df_cities, df_states)
    df = ["%s, %s" % x for x in df]
    df = str(df).strip('[]')

    print("The cities that are the warmest in July are: {0}".format(df))




