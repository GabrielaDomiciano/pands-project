import matplotlib.pyplot as plt
import pandas as pd

# Load the Data
iris_df = pd.read_csv('iris-data.csv')
print(iris_df)

# Empty columns were deleted.
iris_df = iris_df.dropna()
print(iris_df)



