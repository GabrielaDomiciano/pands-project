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

# Print the first 10 lines of the DataFrame
print(iris_df.head(10))


# Calculates descriptive statistics, and saves it to a CSV file called 'summary.csv'
summary = iris_df.describe().T
summary.to_csv('summary.csv')

# Print the shape, number of rows and columns in the DataFrame.
shape_iris = iris_df.shape
print(iris_df.shape)

columns = iris_df.columns
print(columns)

#missing Values
missing_values = iris_df.isna().any()
print(missing_values)


# Inspect types.
type = iris_df.dtypes
print(type)


# Describing the setosa class
iris_setosa = iris_df.loc[iris_df["species"]=="setosa"]
print(iris_setosa.describe()) 

# Describing the versicolor class
iris_versicolor = iris_df.loc[iris_df["species"]=="versicolor"]
print(iris_versicolor.describe()) 

# Describing the virginica class
iris_virginica = iris_df.loc[iris_df["species"]=="virginica"]
print(iris_virginica.describe())

# Number the flower per species.
plt.plot(iris_df['species'])
plt.xlabel("lines")
plt.savefig('Specie_line')
plt.show()
count = iris_df['species'].value_counts()
print(count)
iris_df['species'].value_counts().plot(kind='bar')
plt.title('Number of Species')
plt.legend(title='Quantity per Species', labels=count)
plt.savefig('Quantity per Species')
plt.show()


# Checking for the unique values.
uniq_iris = iris_df.nunique()
print(uniq_iris)


# Scatter plots
sns.pairplot(iris_df,hue="species")
plt.savefig('pairplot')
plt.show()


# Plotting the distplot 
sns.histplot(iris_df['sepal_length'], color='pink')
sns.histplot(iris_df["sepal_length"], kde=True, color='blue')
plt.savefig('Histplot sepal_len')
plt.show()

sns.histplot(iris_df['sepal_width'], color='pink')
sns.histplot(iris_df["sepal_width"], kde=True, color='blue')
plt.savefig('Histplot setal_wid')
plt.show()

sns.histplot(iris_df['petal_length'], color='pink')
sns.histplot(iris_df["petal_length"], kde=True, color='blue')
plt.savefig('Histplot petal_len')
plt.show()

sns.histplot(iris_df['petal_width'], color='pink')
sns.histplot(iris_df["petal_width"], kde=True, color='blue')
plt.savefig('Histplot petal_wid')
plt.show()


petal_length = iris_df['petal_length']
print(petal_length)


# Just get the numpy array.
petal_lengthNP = petal_length.to_numpy()
print(petal_lengthNP)


# Lets see the petal width.
petal_width = iris_df['petal_width']
print(petal_width)


# Petal widths.
petal_widthNP = iris_df['petal_width'].to_numpy()
print(petal_widthNP)


# The petal_length per species.
petal_len = iris_df[['species', 'petal_length']]
print(petal_len)


# The sepal_length per species.
sepal_length = iris_df[['species', 'sepal_length']]
print(sepal_length)



# Simple plot.
plt.plot(petal_length, petal_width, 'x', color='green')
plt.savefig('Petal_length_width')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Iris Data')
plt.xlim(0, 8)
plt.ylim(0, 4)



# Create a new figure and set of axes.
fig, ax = plt.subplots()
ax.plot(petal_length, petal_width, 'x', color='green')
plt.savefig('Subplots')
ax.set_xlabel('Petal Length')
ax.set_ylabel('Petal Width')
ax.set_title('Iris Data Set')
ax.set_xlim(0, 8)
ax.set_ylim(0, 4)


# Fit a line between x and y.
m, c = np.polyfit(petal_length, petal_width, 1)
print(m, c)
print("Slope (m):", m)
print("Intercept (c):", c)

# Creates a series of values along the line of best fit, generating 100 points spaced between 0.0 and 8.0.
line_x = np.linspace(0.0, 8.0, 100)
line_y = m * line_x + c

# Create a new figure and set of axes.
fig, ax = plt.subplots()


#  plot.
ax.plot(petal_length, petal_width, 'x', color='green')
ax.plot(line_x, line_y, 'r-')
plt.savefig('Plot petal_length petal_width.png')
ax.set_xlabel('Petal Length')
ax.set_ylabel('Petal Width')
ax.set_title('Iris Data')
ax.set_xlim(0, 8)
ax.set_ylim(-1, 4)
plt.show()


#  Boxplot 
sns.boxplot(x='species',y='sepal_length',data=iris_df)
plt.grid()
plt.savefig('Specie sepal length')
plt.show()

sns.boxplot(x='species',y='sepal_width',data=iris_df)
plt.grid()
plt.savefig('Specie sepal width')
plt.show()

sns.boxplot(x='species',y='petal_width',data=iris_df)
plt.grid()
plt.savefig('Species petal width')
plt.show()

sns.boxplot(x='species',y='petal_length',data=iris_df)
plt.grid()
plt.savefig('Species petal length')
plt.show()


# scatter plot 
plt.figure(figsize=(8,6))
sns.scatterplot(data=iris_df, x='petal_length', y='petal_width', hue='species')
plt.title('Petals Width vs Length')
plt.xlabel('Width')
plt.ylabel('Length')
plt.legend(bbox_to_anchor=(1, 1), loc=2) 
plt.savefig('Petals Width vs Length.png')
plt.show()


plt.figure(figsize=(8,6))
sns.scatterplot(data=iris_df, x= 'sepal_length', y= 'petal_width', hue= 'species')
plt.title('Sepals Width vs Length')
plt.xlabel('Width')
plt.ylabel('Length')
plt.savefig('Sepals Width vs Length.png')
plt.show() 

