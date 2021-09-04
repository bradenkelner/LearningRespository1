# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 17:44:16 2021

@author: kelnerb



conda install pandas
conda install numpy
conda install scipy
conda install matplotlib
conda install seaborn



"""

import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
# %%

data = pd.read_csv("iris.csv")
sepal_length = np.array(data["sepal.length"])
sepal_width = np.array(data["sepal.width"])

np.mean(sepal_length)
np.std(sepal_length)

np.mean(sepal_width)
np.std(sepal_width)

sns.histplot(data=sepal_length, binrange =[4,8], binwidth = .25, kde=True,color= "#911111"  )
sns.histplot(data=sepal_width)


sns.ecdfplot(data=sepal_width)
sns.boxplot(data=sepal_width)












