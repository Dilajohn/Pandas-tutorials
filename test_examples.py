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

#Select the first row of data (the first record) from reviews, assigning it to the variable first_row
first_row = reviews.iloc[0]
print(first_row)

"""4.
Select the first 10 values from the description column in reviews, assigning the result to variable first_descriptions.
Hint: format your output as a pandas Series"""

first_descriptions = reviews.description.iloc[:10]
print(first_descriptions)

#Note that many other options will return a valid result, such as desc.head(10) and reviews.loc[:9, "description"]. 
ops_description = desc.head(10)
print(ops_description)

ops_2_description = reviews.loc[:9, "description"]
print(ops_2_description)


#Select the records with index labels 1, 2, 3, 5, and 8, assigning the result to the variable sample_reviews.
#In other words, generate the following DataFrame:
sample_reviews = reviews.iloc[[1,2,3,5,8]]
print(sample_reviews)
