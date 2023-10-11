# %% [markdown]
# live_Pandas Tips and Tricks

# %%
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

# %%
df = sns.load_dataset('titanic')
df

# %% [markdown]
# Basic Information

# %%
df.info()

# %%
df.columns

# %%
df.describe()

# %%
# Missing Values and NaN/ Null Values

df.isnull().sum() # Count the missing values

# %%
#Percentage of Null values in a columns
df.isnull().sum() / len(df) * 100

# %%
# Another way to find null values 
sns.heatmap(df.isnull(), cbar= False)

# %%
# Find Out unique Values
df.head()

# %%
# Find Out unique Values
df['sex'].unique()

# %%
df[['sex','age','fare']]

# %%
df['sex'].nunique() # find number of unique values

# %%
df.sex.nunique()

# %%
df.nunique() # To find ALl the columns number unique values

# %%
df.columns # Print coloumns name 

# %%
df['embark_town'].unique()

# %%
# Value Count
df['embark_town'].value_counts()

# %%
df.head()

# %%
# Groupby Function

df.groupby('class')['fare'].mean()

# %%
# Survived  Fare
df.groupby('survived')['fare'].mean()

# %%
# Group byy two columns
df.groupby(['sex', 'who'])['fare'].value_counts()

# %%
# Group byy two columns
df.groupby(['survived', 'who']).size()

# %%
# Corealtion MAtrix
df_cor = df[['fare','age','sibsp', 'parch']].corr()

# %%
df_cor

# %%
sns.heatmap(df_cor , annot=True )

# %%
sns.pairplot(df)

# %%
sns.histplot(df)

