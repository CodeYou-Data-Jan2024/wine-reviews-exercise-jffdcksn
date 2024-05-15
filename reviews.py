import pandas as pd
import zipfile

reviews = pd.read_csv('data/winemag-data-130k-v2.csv.zip', compression='zip')

summary = reviews.groupby('country').agg({'title':'count', 'points':'mean'}).round(1)

summary = summary.rename(columns= {'title' : 'count'}).reset_index()

summary = summary.sort_values('count', ascending=False)


summary.to_csv('data/reviews-per-country.csv', index=False)




print(summary)

