
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# Iris dataset contains five columns such: as Petal Length, Petal Width, Sepal Length, Sepal Width and Species Type.

sys.stdout = open ("analysis_summary.txt","w")

iris = pd.read_csv('iris.csv')

print ("------------------------------------------------------------------------------")
print ("Summary of the entire dataset:")
print ("------------------------------------------------------------------------------")
print ("\n")
print(iris)
print ("\n")
print ("------------------------------------------------------------------------------")
# reference for .describe() and .info(): https://towardsdatascience.com/getting-started-to-data-analysis-with-python-pandas-with-titanic-dataset-a195ab043c77
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
# reference for idea: https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
print (iris['variety'].value_counts())
print ("\n")
print ("------------------------------------------------------------------------------")
sys.stdout.close()