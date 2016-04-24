import collections
import pandas

# population_dict = collections.defaultdict(int)
# with open('/Users/chrisdorman/PycharmProjects/Thinkful/Data_Science/'
#           'lecz-urban-rural-population-land-area-estimates-v2-csv/'
#           'lecz-urban-rural-population-land-area-estimates_continent-'
#           '90m.csv','rU') as inputfile:
#     header = next(inputfile)
#     for line in inputfile:
#         line = line.rstrip().split(',')
#         line[5] = int(line[5])
#         if line[1] == 'Total National Population':
#             population_dict[line[0]] += line[5]

import pandas as pd

input_dataframe = pd.read_csv('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv')

print input_dataframe[:10]