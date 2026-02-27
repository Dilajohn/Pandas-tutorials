import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)   # Load the CSV file into a DataFrame,
#print(reviews.head()) # Print the first few rows of the DataFrame to get an overview of the data

pd.set_option("display.max_rows", 5)  # Set the maximum number of rows to display to 5
#print(reviews)  # Print the DataFrame to see the effect of the new display option

#---- ACCESSING THE PROPERTY OF A DATAFRAME ---

#print(reviews.country)  # Access the 'country' column of the DataFrame, which returns a Series
#print(reviews["country"])  # Access the 'country' column using bracket notation, which also returns a Series
#print(reviews["country"][0])  # Access the first element of the 'country' column, which returns the country of the first review


#--Indexing in pandas--
""" The indexing operator and attribute selection are nice because they work just like they do in the rest of the Python ecosystem.
As a novice, this makes them easy to pick up and use. However, pandas has its own accessor operators, loc and iloc. For more advanced operations,
these are the ones you're supposed to be using.


Indexing in pandas

The indexing operator and attribute selection are nice because they work just
like they do in the rest of the Python ecosystem. As a novice, this makes them easy to pick up and use. However,
pandas has its own accessor operators, loc and iloc. For more advanced operations, these are the ones you're supposed to be using.
Index-based selection

Pandas indexing works in one of two paradigms. The first is index-based selection: 
selecting data based on its numerical position in the data. iloc follows this paradigm.

To select the first row of data in a DataFrame, we may use the following:
reviews.iloc[0]  # Select the first row of the DataFrame using iloc, which returns a Series representing the first review

"""
#print(reviews.iloc[0])  # Select the first row of the DataFrame using iloc, which returns a Series representing 
                        #the first review

""" Both loc and iloc are row-first, column-second. This is the opposite of what we do in native Python,
which is column-first, row-second.

This means that it's marginally easier to retrieve rows, and marginally harder to get retrieve columns.
To get a column with iloc, we can do the following """

#print(reviews.iloc[:, 0])  # Select the first column of the DataFrame using iloc, which returns a Series
                           #representing the 'country'
                           
""" On its own, the : operator, which also comes from native Python, means "everything".
When combined with other selectors, however, it can be used to indicate a range of values. 
For example, to select the country column from just the first, second, and third row, we would do"""

#print(reviews.iloc[:3,0])  # Select the first three rows of the first column of the DataFrame using iloc,
                           #which returns a Series
                           

#Or, to select just the second and third entries, we would do:

#print(reviews.iloc[1:3,0])  # Select the second and third rows of the first column of the DataFrame using iloc,
                           #which returns a Series




#It's also possible to pass a list of integers to iloc. This allows us to select specific rows and
# columns by their integer position. For example, to select the first and third rows of the first column, we would do:
print(reviews.iloc[[1,2,3],0])  # Select the second, third, and fourth rows of the first column of the DataFrame using
                                #iloc,
                                #which returns a Series
                                
#Finally, it's worth knowing that negative numbers can be used in selection.
# This will start counting forwards from the end of the values.
# So for example here are the last five elements of the dataset
print(reviews.iloc[-5:0])  # Select the last five rows of the DataFrame using iloc, which returns a DataFrame