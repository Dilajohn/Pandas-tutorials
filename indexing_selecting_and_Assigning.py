import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)   # Load the CSV file into a DataFrame,
#print(reviews.head()) # Print the first few rows of the DataFrame to get an overview of the data

pd.set_option("display.max_rows", 5)  # Set the maximum number of rows to display to 5
#print(reviews)  # Print the DataFrame to see the effect of the new display option

#---- ACCESSING THE PROPERTY OF A DATAFRAME ---

#print(reviews.country)  # Access the 'country' column of the DataFrame, which returns a Series
#print(reviews["country"])  # Access the 'country' column using bracket notation, which also returns a Series
print(reviews["country"][0])  # Access the first element of the 'country' column, which returns the country of the first review