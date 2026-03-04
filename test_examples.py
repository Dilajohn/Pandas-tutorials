import pandas as pd

wines_reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)   # Load the CSV file into a DataFrame,

#Look at an overview of your data by running the following line
print(wines_reviews.info)  # Print a concise summary of the DataFrame,
                           #including the number of non-null entries and data types of each column