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

#Select the first value from the description column of reviews, assigning it to variable first_description
first_description = reviews.description[0]
print(first_description)
"""first_description = reviews.description.iloc[0]
Note that while this is the preferred way to obtain the entry in the DataFrame, 
many other options will return a valid result, such as reviews.description.loc[0], reviews.description[0]"""
Second_description = reviews.description.iloc[0]
print(Second_description)

Third_description = reviews.description.loc[0]
print(Third_description)

Fourth_description = reviews.description[0]
print(Fourth_description)
