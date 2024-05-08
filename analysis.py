# Gabriela Domiciano

# Exploratory Analysis: Iris Data_set
# Import required packages:
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Let's take a look at the Dataset.
iris_df = pd.read_csv('iris-data.csv')
#print(iris_df)

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
missing_values = iris_df.isna().any()
#print(missing_values)

# Inspect types.
type = iris_df.dtypes
#print(type)


# Lets see the petal length.
petal_length = iris_df['petal_length']
#print(petal_length)

# Lets see the petal width.
petal_width = iris_df['petal_width']
#print(petal_width)

## Number the flower per species.
count = iris_df['species'].value_counts()
#print(count)

# The petal_length per species.
petal_length = iris_df[['species', 'petal_length']]
# Show.
#print(petal_length)

# The sepal_length per species.
sepal_length = iris_df[['species', 'sepal_length']]
# Show.
#print(sepal_length)

'''
# The plots below show the relationships between the width and length of petals and sepals of species.

# Sets the figure size and creates a scatter plot showing the relationship between petal width and length,
# with different iris species represented by different colors.
plt.figure(figsize=(8,6))
sns.scatterplot(data = iris_df, x ='petal_length', y ='petal_width', hue ='species')
plt.title('Petals Width vs Length')
plt.xlabel('Width')
plt.ylabel('Length')
plt.savefig('Petals Width vs Length')
plt.show()



# This code creates a scatterplot using seaborn to visualize the relationship 
# between sepal length and petal width of flowers, with different colors for each species.
plt.figure(figsize=(8,6))
sns.scatterplot(data = iris_df, x = 'sepal_length', y = 'petal_width', hue = 'species')
plt.title('Sepals Width vs Length')
plt.xlabel('Width')
plt.ylabel('Length')
plt.savefig('Sepals Width vs Length')
plt.show()
'''