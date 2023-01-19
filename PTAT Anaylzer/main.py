
from enum import auto
from operator import truediv
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
 


Location = str(input("enter the location: ")) 
# read data from an Excel file
df = pd.read_csv(Location)

 
print(df.head(1))
# prochot

# df['sum'] = df.sum(axis=5)
# print(df['sum'])

# create a line plot
x1 = str(input("xlabel: "))
y1 = str(input("ylabel: "))
# Time



# plt.bar(df[x1],df[y1])

 

# add a title and labels
plt.title("freq gra")
plt.xlabel("TIME")
plt.ylabel("cpu 0 f")

df.plot(x='Time', y='CPU1-Frequency(MHz)', kind='scatter')

# plt.title("freq gra")
# plt.xlabel("TIME")
# plt.ylabel("cpu 1 f")
# # show the plot
plt.show()
