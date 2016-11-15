import nltk
import csv

in_file = csv.DictReader(open('/Users/chrisdorman/PycharmProjects/Thinkful/git/Data_Science/bloomberg_analytics_20161109.csv'))

for row in in_file:
