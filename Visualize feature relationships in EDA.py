import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")
print(df.head()) 
print(df.describe())  
print(df.info()) 

sns.pairplot(df, hue="species")  
plt.show()
