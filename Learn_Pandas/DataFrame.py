# DataFrames
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

# Series is like a column, a DataFrame is the whole table.

# A Pandas DataFrame is a 2 dimensional data structure,
# like a 2 dimensional array, or a table with rows and columns.

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)

#  use loc to return one or more rows
print(myvar.loc[0]) #Note: This example returns a Pandas Series.

#use a list of indexes:
# print(df.loc[[0, 1]]) #Return row 0 and 1:
# Named Indexes
# With the index argument, you can name your own indexes.
data = {
     "calories": [249 ,456 ,76],
      "duration": [50 ,45 ,32] 
 }


df = pd.DataFrame(data,index=["d1","d2","d3"]);# haka bah tmed lkol  row name ta3o
print(df)
print(df.loc[["d1","d2"]]) #Return row d1: loc jaya min locate 

#Load Files Into a DataFrame
# If your data sets are stored in a file, 
# Pandas can load them into a DataFrame.
df = pd.read_csv('C:\\Users\\hp\\Desktop\\Python-data_scince\\Learn_Pandas\\Lists of companies using AI and Data Science in Algeria - List of companies.csv')

print(df.to_string()) 


