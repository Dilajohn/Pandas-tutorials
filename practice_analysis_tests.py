import pandas as pd

wines_reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)   # Load the CSV file into a DataFrame,
                                                                       #using the first column as the index
print(wines_reviews.info)  # Print a concise summary of the DataFrame,
                           #including the number of non-null entries and data types of each column
                           
print(wines_reviews.describe)  # Print a statistical summary of the DataFrame, including count, mean, std, min,
                               #25%, 50%, 75%, and max values for each numeric column
                               
print(wines_reviews.head())  # Print the first few rows of the DataFrame to get an overview of the data 

print(pd.DataFrame({'yes': [50, 24, 75], 'No' : [43, 78, 12]})) 

print(pd.DataFrame({"Bob": ['hello', "I'm Bob the builder", "I can build anything you want"],
                    "Alice": ['hello', 'I am Alice the builder', 'I can build anything you want']},
                    index = ['greeting', 'introduction', 'offer']))  

print(pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])) 

cost = [1000, 2000, 3000, 4000, 5000]
index = ["2015 Sales", "2016 Sales", "2017 Sales", "2018 Sales", "2019 Sales"]
name = "Cost"
print(pd.Series(cost, index=index, name=name))         
                               
print(wines_reviews.columns)  # Print the column names of the DataFrame, which can be useful for 
                              #understanding the structure of the data and for selecting specific columns for analysis.
                              

print(wines_reviews.index)  # Print the index of the DataFrame, which can be useful for understanding the 
                            #structure of the data and for selecting specific rows for analysis.
  
print(wines_reviews.dtypes)  # Print the data types of each column in the DataFrame, which can be useful for
                              #understanding
                              #the types of data you are working with and for selecting appropriate methods 
                              # for analysis.
                              
print(wines_reviews.shape)  # Print the shape of the DataFrame, which is a tuple representing the number of rows
                            #and columns in the DataFrame. This can be useful for understanding the size of the data and for selecting 
                            #appropriate methods for analysis.
print(wines_reviews.size)  # Print the total number of elements in the DataFrame, which is the product of the 
                           #number of rows and columns.
                           
print(wines_reviews.values)  # Print the values of the DataFrame as a NumPy array, which can be useful for performing numerical operations 
                             #on the data or for converting the DataFrame to a different format for analysis.

print(wines_reviews.info)  # Print a concise summary of the DataFrame, including the number of non-null entries and
                           #data types of each column.
                           
print(wines_reviews.describe)  # Print a statistical summary of the DataFrame, including count, mean, std, min,
                               #25%, 50%, 75%, and max values for each numeric column.
                               
print(wines_reviews.iloc[2])
print(wines_reviews.iloc[:, 3])  # Select all rows of the fourth column of the DataFrame using iloc, which returns 
                                 #a Series
                                
#selecting wines from only Italy and France 
print(wines_reviews.loc[wines_reviews.country.isin(["Italy", "France "])])