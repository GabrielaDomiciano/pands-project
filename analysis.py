# Gabriela Domiciano

# Exploratory Analysis: Iris Data_set
# Import required packages:
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Let's take a look at the Dataset.
iris_df = pd.read_csv('iris-data.csv')
print(iris_df)

# Empty columns were deleted, deleting these columns helps in viewing the DataFrame.
iris_df = iris_df.dropna()
#print(iris_df)

# Calculates descriptive statistics, and saves it to a CSV file called 'summary.csv'
#iris_df.describe().T.to_csv('summary.csv')

# Print the first 10 lines of the DataFrame
#print(iris_df.head(10))

# Print the shape, number of rows and columns in the DataFrame.
#print(iris_df.shape)

# Checks for missing values ​​in any column of DataFrame 'iris_df'
#missing_values = iris_df.isna().any()
#print(missing_values)

# Sets the figure size and creates a scatter plot showing the relationship between petal width and length,
# with different iris species represented by different colors.

plt.figure(figsize=(8,6))
sns.scatterplot(data = iris_df, x ='petal_length', y ='petal_width', hue ='species')
plt.title('Petals Width vs Length')
plt.xlabel('Width')
plt.ylabel('Length')
plt.show()
