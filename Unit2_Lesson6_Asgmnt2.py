import pandas as pd
import numpy as np

df = pd.read_csv('/Users/chrisdorman/PycharmProjects/Thinkful/git/Data_Science/LoanStats3b.csv', header=1, low_memory=False)

# converts string to datetime object in pandas:
df['issue_d_format'] = pd.to_datetime(df['issue_d'])
dfts = df.set_index('issue_d_format')
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']

print loan_count_summary