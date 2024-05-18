
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys


# This code redirects the standard output (sys.stdout) to a file named analysis_summary.txt. Any output from print statements will be written to this file.
# reference: https://www.askpython.com/python/python-stdin-stdout-stderr
sys.stdout = open ("analysis_summary.txt","w")

iris = pd.read_csv('iris.csv')

# Iris dataset contains five columns such: as Petal Length, Petal Width, Sepal Length, Sepal Width and Species Type.
print ("------------------------------------------------------------------------------")
print ("Summary of the entire dataset:")
print ("------------------------------------------------------------------------------")
print ("\n")
print(iris)
print ("\n")
print ("------------------------------------------------------------------------------")
print ("Unique classification/type:")
print ("------------------------------------------------------------------------------")
print ("\n")
print (iris['variety'].unique())
print ("\n")
print ("------------------------------------------------------------------------------")
print ("Describe the dataset:")
print ("------------------------------------------------------------------------------")
print ("\n")
print (iris.describe())
print ("\n")
print ("------------------------------------------------------------------------------")
print("Number of occurances of each type:")
print ("------------------------------------------------------------------------------")
print ("\n")
print (iris['variety'].value_counts())
print ("\n")
print ("------------------------------------------------------------------------------")

sys.stdout.close()
# Plotting histogram for Sepal Width

# Load the Iris dataset
iris = pd.read_csv('iris.csv')

# Select and filter the DataFrame to extract the sepal width measurements for each species (Setosa, Versicolor, and Virginica).
setosa = iris[iris['variety'] == 'Setosa']['sepal.width']
versicolor = iris[iris['variety'] == 'Versicolor']['sepal.width']
virginica = iris[iris['variety'] == 'Virginica']['sepal.width']

plt.figure(figsize=(7,5))
plt.hist([setosa, versicolor, virginica], bins=10, label=['Setosa', 'Versicolor', 'Virginica'], color=['pink','royalblue', 'mediumpurple'], edgecolor='black', density=True)
plt.legend()
plt.title('Differences in Sepal Width', fontsize=14)
plt.xlabel('Sepal Width (cm)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.savefig("Sepal.Width.png")
plt.show()

# Plotting histogram for Sepal Length
# Load the Iris dataset
iris = pd.read_csv('iris.csv')

# Select and filter the DataFrame to extract the sepal length measurements for each species (Setosa, Versicolor, and Virginica).
setosa = iris[iris['variety'] == 'Setosa']['sepal.length']
versicolor = iris[iris['variety'] == 'Versicolor']['sepal.length']
virginica = iris[iris['variety'] == 'Virginica']['sepal.length']

plt.figure(figsize=(7,5))
plt.hist([setosa, versicolor, virginica], bins=10, label=['Setosa', 'Versicolor', 'Virginica'], color=['pink','royalblue', 'mediumpurple'], edgecolor='black', density=True)
plt.legend()
plt.title('Differences in Sepal Length', fontsize=14)
plt.xlabel('Sepal Length (cm)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.savefig("Sepal.Length.png")
plt.show()

# Plotting histogram for Petal Width

# Load the Iris dataset
iris = pd.read_csv('iris.csv')

# Select and filter the DataFrame to extract the petal width measurements for each species (Setosa, Versicolor, and Virginica).
setosa = iris[iris['variety'] == 'Setosa']['petal.width']
versicolor = iris[iris['variety'] == 'Versicolor']['petal.width']
virginica = iris[iris['variety'] == 'Virginica']['petal.width']

plt.figure(figsize=(7,5))
plt.hist([setosa, versicolor, virginica], bins=10, label=['Setosa', 'Versicolor', 'Virginica'], color=['pink','royalblue', 'mediumpurple'], edgecolor='black', density=True)
plt.legend()
plt.title('Differences in Petal Width', fontsize=14)
plt.xlabel('Petal Width (cm)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.savefig("Petal.Width.png")
plt.show()

# Plotting histogram for Petal Length
# Load the Iris dataset
iris = pd.read_csv('iris.csv')

# Select and filter the DataFrame to extract the petal length measurements for each species (Setosa, Versicolor, and Virginica).
setosa = iris[iris['variety'] == 'Setosa']['petal.length']
versicolor = iris[iris['variety'] == 'Versicolor']['petal.length']
virginica = iris[iris['variety'] == 'Virginica']['petal.length']

plt.figure(figsize=(7,5))
plt.hist([setosa, versicolor, virginica], bins=10, label=['Setosa', 'Versicolor', 'Virginica'], color=['pink','royalblue', 'mediumpurple'], edgecolor='black', density=True)
plt.legend()
plt.title('Differences in Petal Length', fontsize=14)
plt.xlabel('Petal Length (cm)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.savefig("Petal.Length.png")
plt.show()

# Scatterplots
# Load the Iris dataset
iris = pd.read_csv('iris.csv')

# Create a scatter plot for the relationship between petal length and petal width
plt.figure(figsize=(8, 6))
sns.scatterplot(data=iris, x='petal.length', y='petal.width', hue='variety', palette=["pink","royalblue", "mediumpurple"], s=100)

# Add title and labels
plt.title('Relationship between Petal Length and Petal Width', fontsize=10)
plt.xlabel('Petal Length (cm)', fontsize=10)
plt.ylabel('Petal Width (cm)', fontsize=10)

# Display the plot
plt.legend(title='Variety')
plt.savefig("Petal.Length&Width.png")
plt.show()

# Load the Iris dataset
iris = pd.read_csv('iris.csv')

# Create a scatter plot for the relationship between sepal length and sepal width
plt.figure(figsize=(8, 6))
sns.scatterplot(data=iris, x='sepal.length', y='sepal.width', hue='variety', palette=["pink","royalblue", "mediumpurple"], s=100)

# Add title and labels
plt.title('Relationship between Sepal Length and Sepal Width', fontsize=10)
plt.xlabel('Sepal Length (cm)', fontsize=10)
plt.ylabel('Sepal Width (cm)', fontsize=10)

# Display the plot
plt.legend(title='Variety')
plt.savefig("Sepal.Length&Width.png")
plt.show()

# Create pairplot
pplot = sns.pairplot(iris, hue="variety", palette=["pink","royalblue", "mediumpurple"])

# Show the plot
plt.savefig("Iris.pairplot.png")
plt.show()


