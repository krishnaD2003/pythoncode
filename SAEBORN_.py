import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
sns.get_dataset_names()
df=sns.load_dataset('tips')
df
sns.barplot(x='day',y='total_bill',data=df)
plt.grid()
