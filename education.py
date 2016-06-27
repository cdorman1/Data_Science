from bs4 import BeautifulSoup
import csv
import numpy as np
import pandas as pd
import requests
import sqlite3 as lite


url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"

r = requests.get(url)

soup = BeautifulSoup(r.content)

soup = soup('table')[6]

# get column names from header information
header = soup.find('tr', {'class': 'lheader'})
col_names = [col.string for col in header.find_all('td') if col.string is not None]

# get data from html table
table_a = soup.find_all('tr', {'class': 'tcont'})

table_b = [row for row in table_a if len(row) == 25]

data = []
for row in table_b:
    col = row.find_all('td')
    Country = col[0].string
    Year = col[1].string
    Total = col[4].string
    Men = col[7].string
    Women = col[10].string
    data.append((Country, Year, Total, Men, Women))

education_table = pd.DataFrame(data, columns=col_names)
education_table = education_table.dropna(axis=1, how='all')


con = lite.connect('/Users/chrisdorman/PycharmProjects/Thinkful/git/Data_Science/U3_L3_A2.db')
cur = con.cursor()

with con:
    cur.execute("DROP TABLE IF EXISTS gdp")
    cur.execute(
        'CREATE TABLE gdp (country REAL, GDP_1999 INT, GDP_2000 INT, GDP_2001 INT, GDP_2002 INT, GDP_2003 INT, GDP_2004 INT, GDP_2005 INT, GDP_2006 INT, GDP_2007 INT, GDP_2008 INT, GDP_2009 INT, GDP_2010 INT);')

with open('/Users/chrisdorman/PycharmProjects/Thinkful/git/Data_Science/API_NY.GDP.MKTP.CD_DS2_en_csv_v2/API_NY.GDP.MKTP.CD_DS2_en_csv_v2.csv') as inputFile:
    # skip the first 5 lines
    for n in range(5):
        next(inputFile)
    inputReader = csv.reader(inputFile)
    count = 0
    for line in inputReader:
        # print line
        # count += 1
        # if count == 3:
        #     break
        with con:
            cur.execute('INSERT INTO gdp (country, GDP_1999, GDP_2000, GDP_2001, GDP_2002, GDP_2003, GDP_2004, GDP_2005,'
                        ' GDP_2006, GDP_2007, GDP_2008, GDP_2009, GDP_2010) VALUES ("' + line[0] + '","' + '","'.join(line[43:-6]) + '");')


sql_statement = 'select * from gdp'
table_gdp = pd.read_sql(sql_statement, con)
table_gdp = table_gdp.dropna(axis=1, how='all')

## common countries
list1 = list(set(education_table['Country or area'].tolist()))
list2 = list(set(table_gdp['country'].tolist()))
list_common_countries = list(set(list1) & set(list2))

gdp = []
education_total = []
education_men = []
education_women = []
for country in list_common_countries:
    df1 = education_table[education_table['Country or area'] == country]
    df2 = table_gdp[table_gdp['country'] == country]
    if df2['GDP_' + df1['Year'].irow(0)].irow(0) != '':
        education_total.append(int(df1['Total'].irow(0)))
        education_men.append(int(df1['Men'].irow(0)))
        education_women.append(int(df1['Women'].irow(0)))
        gdp.append(np.log(df2['GDP_' + df1['Year'].irow(0)].irow(0)))

df_final = pd.DataFrame({'Total': education_total, 'Men': education_men, 'Women': education_women, 'gdp': gdp})

print df_final.corr()