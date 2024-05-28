from pandas import read_csv

data = read_csv('f.csv', delimiter='|')
unique_rows = data.drop_duplicates().to_dict('records')
same_id_rows = data.groupby(['id']).max().to_dict('records')
