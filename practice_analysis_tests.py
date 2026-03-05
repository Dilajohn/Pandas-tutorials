import pandas as pd

wines_reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)   # Load the CSV file into a DataFrame,
                                                                       #using the first column as the index
print(wines_reviews.info)  # Print a concise summary of the DataFrame,
                           #including the number of non-null entries and data types of each column
                           
print(wines_reviews.describe)  # Print a statistical summary of the DataFrame, including count, mean, std, min,
                               #25%, 50%, 75%, and max values for each numeric column
