import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("clothing_store.csv")

# Overview
print(df.info())
print(df.describe())

# Top-selling categories
print(df['category'].value_counts().head())

# Revenue by category
revenue = df.groupby('category')['price'].sum().sort_values(ascending=False)
print(revenue)

# Visualize top 5 categories by revenue
revenue.head().plot(kind='bar', title='Top Categories by Revenue')
plt.ylabel("Revenue")
plt.xlabel("Category")
plt.tight_layout()
plt.show()
