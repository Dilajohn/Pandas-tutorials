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
                               
                               
