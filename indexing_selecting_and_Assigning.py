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
print(reviews.iloc[-5:])  # Select the last five rows of the DataFrame using iloc, which returns a DataFrame


"""
Label-based selection

The second paradigm for attribute selection is the one followed by the loc operator: label-based selection.
In this paradigm, it's the data index value, not its position, which matters. This means that the first row of data is
not necessarily the row with index 0, and the first column of data is not necessarily the column with index 0.

iloc is conceptually simpler than loc because it ignores the dataset's indices. When we use iloc we treat 
the dataset like a big matrix (a list of lists), one that we have to index into by position. loc, by contrast,
uses the information in the indices to do its work. Since your dataset usually has meaningful indices, 
it's usually easier to do things using loc instead. For example, here's one operation that's much easier using loc:
"""
#print(reviews.loc[:,['taster_name', 'taster_twitter_handle', 'points']])

"""
Manipulating the index¶

Label-based selection derives its power from the labels in the index. Critically, the index we use is not immutable. We can manipulate the index in any way we see fit.

The set_index() method can be used to do the job. Here is what happens when we set_index to the title field:
"""

#print(reviews.set_index('title'))  # Set the index of the DataFrame to the 'title' column using set_index, 
                                   #which returns a new DataFrame with the new index
                                   
"""Conditional selection

So far we've been indexing various strides of data, using structural properties of the DataFrame itself.
To do interesting things with the data, however, we often need to ask questions based on conditions.

For example, suppose that we're interested specifically in better-than-average wines produced in Italy.

We can start by checking if each wine is Italian or not:"""

#print(reviews.country == "Italy")  # Create a boolean Series indicating whether each wine is from Italy by
                                   #comparing the 'country' column to the string "Italy"
                                   
"""This operation produced a Series of True/False booleans based on the country of each record.
This result can then be used inside of loc to select the relevant data:"""

#print(reviews.loc[reviews.country =="Italy"])  # Select all rows of the DataFrame where the 'country' column is equal
                                               #to "Italy" using loc,
                                               #which returns a DataFrame of Italian wines
"""This DataFrame has ~20,000 rows. The original had ~130,000. That means that around 15% of wines originate from 
Italy.
We also wanted to know which ones are better than average. Wines are reviewed on a 80-to-100 point scale,
so this could mean wines that accrued at least 90 points.
We can use the ampersand (&) to bring the two questions together"""

#print(reviews.loc[(reviews.country == "Italy") & (reviews.points >= 90)])  # Select all rows of the DataFrame where the
#'country' column is equal to "Italy" and the 'points' column is greater than or equal to 90 using loc,
#which returns a DataFrame of Italian wines with at least 90 points


#Suppose we'll buy any wine that's made in Italy or which is rated above average. For this we use a pipe (|):

#print(reviews.loc[(reviews.country == "Italy") | (reviews.points >= 90)])  # Select all rows of the DataFrame where the

#'country' column is equal to "Italy" or the 'points' column is greater than or equal to 90 using loc,
#which returns a DataFrame of Italian wines or wines with at least 90 points


print(reviews.loc[reviews.country.isin(["Italy", "France"])])
