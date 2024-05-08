# Project Iris Dataset
I study at [ATU](https://www.atu.ie).

![Iris](https://datacrayon.com/assets/images/d3d0e50975c732357668e3e5bb3c5581.jpg)


## Introduction 👋 🌸
This is the final project of the Programming and Scripting course, during the course we learned how to program in Python, and perform data analysis, this project will allow us to put into practice the knowledge, being able to understand and learn how to perform data analysis in practice. 

The dataset shows a set of measurements of the petals and sepals of three flower species: setosa, versicolor and virginica.
The objective in this project is to do an analysis of the dataset, using the Python language.


## Installation 🛠️

To execute the codes, you must have Python installed on your computer. One option is to download Anaconda, which is a free package management environment. It already comes with all the libraries and packages needed to program in Python.

[Anaconda](https://www.anaconda.com).
[Pyhton](https://www.python.org).
[Pandas](https://pandas.pydata.org).
[Numpy](https://numpy.org).
[Matplotlib](https://matplotlib.org).

I used as editor for Python:[VS Code](https://code.visualstudio.com).


## Summary of Variables

Loading the dataset we see that the Dataset contains characteristics of length and width of sepals and petals, from 50 samples of three iris species, Setosa, Virginica and Versicolor.

Lets have a look 👀

![Iris](https://editor.analyticsvidhya.com/uploads/51518iris%20img1.png)

We can visualize the first 10 rows of the Iris dataset and print its shape. This means there are 150 rows and 5 columns in the DataFrame.The result shows the lengths and widths of the iris petals and sepals, indicating, in the last column, which species these measurements belong to.
We want to see a statistical summary. To do this we will use describe(). I used .T to transpose the dataset, transform rows into columns and vice versa.
Note that in the count column, the result was always 150, this could indicate that there are no missing values. To check if there are missing values ​​(NaN) in any column of the iris DataFrame, we can use "isna()".




## References 📚