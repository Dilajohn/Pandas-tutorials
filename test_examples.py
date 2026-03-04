import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)   # Load the CSV file into a DataFrame,

#Look at an overview of your data by running the following line
print(reviews.info)  # Print a concise summary of the DataFrame,
                           #including the number of non-null entries and data types of each column
                           
#Select the description column from reviews and assign the result to the variable desc.
print(reviews.description)
print(reviews['description'])
desc = reviews['description']
print(type(desc))