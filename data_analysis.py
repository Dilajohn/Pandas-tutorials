import pandas as pd

wines_reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)   # Load the CSV file into a DataFrame,
                                                                       #using the first column as the index

print(wines_reviews.head())  # Print the first few rows of the DataFrame to get an overview of the data
#print(wines_reviews)


