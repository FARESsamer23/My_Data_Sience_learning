'''
What is Pandas?
Pandas is a Python library used for working with data sets.

It has functions for analyzing, cleaning, exploring, and manipulating data.

The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.

Why Use Pandas?
Pandas allows us to analyze big data and make conclusions based on statistical theories.

Pandas can clean messy data sets, and make them readable and relevant.

Relevant data is very important in data science.


What Can Pandas Do?
Pandas gives you answers about the data. Like:

Is there a correlation between two or more columns?
What is average value?
Max value?
Min value?



'''
import pandas as pd
# print(pd.__version__)



'''
What is a Series?
A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type.

'''

a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
# yafichalek biha b type ta3ha  sous forme de one-dimensional array holding data of any type

# Create Labels
# With the index argument, you can name your own labels.

# Example
# Create your own labels:



a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

# Key/Value Objects as Series
# You can also use a key/value object, like a dictionary, when creating a Series.

# Example
# Create a simple Pandas Series from a dictionary:

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)
