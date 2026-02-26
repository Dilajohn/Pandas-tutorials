import pandas as pd

wines_reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

#print(wines_reviews.head())
print(wines_reviews)


