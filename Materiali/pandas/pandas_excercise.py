# Start by importing the pandas library and loading a 
# dataset into a DataFrame. You can use one of the built-in
#  datasets from the seaborn library or load a dataset from 
# a CSV file using the pd.read_csv() function.
import pandas as pd
import seaborn as sns

# Load the "titanic" dataset from the seaborn library
df = sns.load_dataset('titanic')
# Copy
# Use the head() method to view the first few rows of the dataset and get a sense of what the data looks like.
# View the first few rows of the dataset
df.head()
# Copy
# Use the info() method to view summary information about the dataset, including the number of rows and columns, the data types of each column, and the number of non-null values in each column.
# View summary information about the dataset
df.info()
# Copy
# Use the describe() method to view summary statistics for the numeric columns in the dataset.
# View summary statistics for the numeric columns
df.describe()
# Copy
# Use boolean indexing to filter the rows in the dataset based on a condition. For example, you could select only the rows where the survived column is equal to 1.
# Select only the rows where "survived" is equal to 1
survived = df[df['survived'] == 1]

# View the first few rows of the filtered dataset
survived.head()
# Copy
# Use the groupby() method to group the rows in the dataset by one or more columns and compute summary statistics for each group. For example, you could group by the sex column and compute the mean value of each numeric column for each group.
# Group by "sex" and compute mean values for each group
df.groupby('sex').mean()
# Copy
# Use the pivot_table() method to create a pivot table that summarizes the data in a different way. For example, you could create a pivot table that shows the mean value of the fare column for each combination of values in the sex and class columns.
# Create a pivot table that shows mean "fare" for each combination of "sex" and "class"
pd.pivot_table(df, values='fare', index='sex', columns='class', aggfunc='mean')
# Copy
# I hope this exercise gives you a good starting point for practicing using pandas. Let me know if you have any questions or if you’d like more guidance on any specific aspect.