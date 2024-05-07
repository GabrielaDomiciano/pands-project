import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Let's take a look at the Dataset.
iris_df = pd.read_csv('iris-data.csv')
print(iris_df)

# Empty columns were deleted, deleting these columns helps in viewing the DataFrame.
iris_df = iris_df.dropna()
print(iris_df)

# Calculates descriptive statistics, and saves it to a CSV file called 'summary.csv'
iris_df.describe().to_csv('summary.csv')

# Print the first 10 lines of the DataFrame
print(iris_df.head(10))

# Print the shape, number of rows and columns in the DataFrame.
print(iris_df.shape)

