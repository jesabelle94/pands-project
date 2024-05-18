# Project Instructions
This repository is dedicated to the pands-project given during the Programming and scripting module on Higher Diploma in Data Analytics course. The project focuses on researching and investigating Fisher's Iris dataset.

## Table Of Contents
- [**Requirements**]()
- [**Fisher's Iris data set**]()
- [**Use of This Project**] ()
- [**Get Help & References**]()
- [**Contribution**]()


## Requirements

To undertake this project, it is necessary to download and install all the required software, as well as set up a GitHub account.
- [Cmder](https://cmder.app/)
- [Anaconda](https://www.anaconda.com/products/individual)
- [Visual Studio Code (VS Code)](https://code.visualstudio.com/Download)
- [GitHub Account](https://github.com/jesabelle94)

## Use Of This Project

This project is useful for getting started with Data Analytics and importantly to demonstrate the following:
- Source and investigate sets of data.
- Programmatically explore and visualize data.
- Apply basic mathematical data analysis techniques to data sets.
- Model real-world problems for analysis by computer.
- Provide evidence in a decision-making process using a data set.
- Appreciate the limitations of graphical representations in data intensive workflows.

## Fisher's Iris Data Set

<img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*lFC_U5j_Y8IXF4Ga87KNVg.png" width="800" height="300"/>

This project is about my analysis of the well-known [Fisher's Iris](https://archive.ics.uci.edu/dataset/53/iris) dataset and the variables in contains. The Iris 
data set is one of the nmost well-known and commonly used datasets in the field of statistics and machine learning. The Iris dataset consists of 150 samples of 
iris flowers from three different species: Setosa, Versicolor, and Virginica. Each sample has four features: sepal length, sepal width, petal length, and petal 
width. Ronald Fisher, a British biologist and statistician, introduced this concept in 1936.

Attribute Information:
1. Sepal length in cm
2. Sepal width in cm
3. Petal length in cm
4. Petal width in cm
5. Variety/Species:
    - Iris Setosa
    - Iris Versicolor
    - Iris Virginica

## Dataset Analysis
 
### Libraries & Modules Used

 The modules and libraries used to undertake the Iris dataset analysis were imported. Each library/module used are explained and referenced throughout when writing the codes. 

    - import numpy as np
    - import pandas as pd
    - import matplotlib.pyplot as plt
    - import seaborn as sns
    - import sys

### Importing Iris Data Set

The project focuses on Iris data set and a [copy of the iris data set csv file](https://archive.ics.uci.edu/dataset/53/iris) was downloaded used to do the 
analysis. The Iris data set was imported using the csv file using pd.read.csv("filepath.csv"). This was used throughout the analysis to get data. 

    iris = pd.read_csv('/Users/jennyformentera/Desktop/pands-project/iris.csv')

### Analysis Summary

Analysis summary is stored in [analysis_summary.txt](https://github.com/jesabelle94/pands-project/blob/main/analysis_summary.txt). This code redirects the standard output (sys.stdout) to a file named analysis_summary.txt. Any output from print statements will be written to this file.
    
   
    sys.stdout = open ("analysis_summary.txt","w")
    iris = pd.read_csv('iris.csv')

       
<details>
Summary of the entire dataset
           <summary>print(iris)</summary>
           <p>

            sepal.length  sepal.width  petal.length  petal.width    variety
            0             5.1          3.5           1.4          0.2     Setosa
            1             4.9          3.0           1.4          0.2     Setosa
            2             4.7          3.2           1.3          0.2     Setosa
            3             4.6          3.1           1.5          0.2     Setosa
            4             5.0          3.6           1.4          0.2     Setosa
            ..            ...          ...           ...          ...        ...
            145           6.7          3.0           5.2          2.3  Virginica
            146           6.3          2.5           5.0          1.9  Virginica
            147           6.5          3.0           5.2          2.0  Virginica
            148           6.2          3.4           5.4          2.3  Virginica
            149           5.9          3.0           5.1          1.8  Virginica

            [150 rows x 5 columns]

</p>
</details>



<details>
Unique classification/types
    <summary>print (iris['variety'].unique())</summary>

    ['Setosa' 'Versicolor' 'Virginica']

</p>
</details>



<details>
Describe the dataset      
    <summary>print (iris.describe())</summary>


       sepal.length  sepal.width  petal.length  petal.width
        count    150.000000   150.000000    150.000000   150.000000
        mean       5.843333     3.057333      3.758000     1.199333
        std        0.828066     0.435866      1.765298     0.762238
        min        4.300000     2.000000      1.000000     0.100000
        25%        5.100000     2.800000      1.600000     0.300000
        50%        5.800000     3.000000      4.350000     1.300000
        75%        6.400000     3.300000      5.100000     1.800000
        max        7.900000     4.400000      6.900000     2.500000


</p>
</details>



<details>
Number of occurances of each type
    <summary>print (iris['variety'].value_counts())</summary>


    variety
    Setosa        50
    Versicolor    50
    Virginica     50
    Name: count, dtype: int64


</p>
</details>

    sys.stdout.close()


### Histograms

Histogram was created for each variable to png files. Four variables were used to present each histogram which are:
    
    - Sepal Width
    - Sepal Length
    - Petal Width
    - Petal Length

Code example used for Histogram:


    # Load the Iris dataset
    iris = pd.read_csv('iris.csv')

    # Select and filter the DataFrame to extract the sepal width measurements for each species (Setosa, Versicolor, and Virginica).
    setosa = iris[iris['variety'] == 'Setosa']['sepal.width']
    versicolor = iris[iris['variety'] == 'Versicolor']['sepal.width']
    virginica = iris[iris['variety'] == 'Virginica']['sepal.width']

    # Create a histogram for the sepal width data of the three species.
    plt.figure(figsize=(7,5))
    plt.hist([setosa, versicolor, virginica], bins=10, label=['Setosa', 'Versicolor', 'Virginica'], color=['pink','royalblue', 'mediumpurple'], edgecolor='black',  density=True)
    plt.legend()
    plt.title('Differences in Sepal Width', fontsize=14)
    plt.xlabel('Sepal Width (cm)', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.show()

<img src = "https://github.com/jesabelle94/pands-project/blob/main/Sepal.Width.png" alt = "Sepal Width" width = "450" height = "450"> <img src = "https://github.com/jesabelle94/pands-project/blob/main/Sepal.Length.png" alt = "Sepal Length" width = "450" height = "450">

<img src = "https://github.com/jesabelle94/pands-project/blob/main/Petal.Width.png" alt = "Petal Width" width = "450" height = "450"> <img src = "https://github.com/jesabelle94/pands-project/blob/main/Petal.Length.png" alt = "Petal Length" width = "450" height = "450">


## Get Help & References 

- [Using Pandas for Statistical Analysis](https://learncodingfast.compython-for-data-science-how-to-output-basic-summary-statistics-using-a-single-pandas-function/)
- [Python - IRIS Data visualization and explanation](https://www.kaggle.com/code/abhishekkrg/python-iris-data-visualization-and-explanation)
- [About Fisher’s Iris dataset](https://www.angela1c.com/projects/iris_project/the-iris-dataset/)
- [Iris Dataset - Exploratory Data Analysis](https://www.kaggle.com/code/lalitharajesh/iris-dataset-exploratory-data-analysis)
- [Iris Data Visualization using Python](https://www.kaggle.com/code/aschakra/iris-data-visualization-using-python)
- [List of named colors](https://matplotlib.org/stable/gallery/color/named_colors.html)
- [How To Create Histograms in Python Using Matplotlib](https://www.nickmccullum.com/python-visualization/histogram/)
 

## Contributions

Jenny Isabelle Formentera.