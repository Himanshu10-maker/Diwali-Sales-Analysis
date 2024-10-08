# -*- coding: utf-8 -*-
"""Diwali Sales analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IjDyEmx3NeFJ3Qov9yTGT5pIV1ewRRXr
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/Diwali Sales Data.csv', encoding="unicode_escape")
df.shape

df.head()

df.info()

#drop unrealted/blank column
df.drop(['Status','unnamed1'],inplace=True,axis=1)

df.info()

#check for null values
pd.isnull(df).sum()

df.shape

#drop null values
df.dropna(inplace=True)

df.shape

#initializew list of list
data_test =[['madhav',11],['keshav',15],['ram',34],['rajesh',]]
#create pandas dataframe using list
df_test = pd.DataFrame(data_test,columns=['Name','Age'])
df_test

df_test.dropna(inplace=True)

df_test

#change data type
df['Amount']=df['Amount'].astype('int')

df['Amount'].dtypes

df.columns

#rename column
df.rename(columns={'Marital_Status':'Shadi'})

#describre method returns description of the data in the dataframe(count,mean.std etc)
df.describe()

#use describe() for specific column
df[['Age','Orders','Amount']].describe()

"""**Exploratory Data Analysis**

**1. Gender**
"""

df.columns

ax = sns.countplot(x='Gender',data=df,hue='Gender', palette={'M': 'blue', 'F': 'red'})

for bars in ax.containers:
    ax.bar_label(bars)

df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sales_gen = df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.barplot(x='Gender',y='Amount',data=sales_gen,hue='Gender',palette={'M': 'orange','F':'blue'})

"""From the above Graphs, we can see that females has made more purchases than men.

**2. Age**
"""

ax=sns.countplot(x='Age Group',data=df,hue='Gender')

 for bars in ax.containers:
     ax.bar_label(bars)

#total amount vs Age group
sales_age = df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.barplot(x ='Age Group',y='Amount',data=sales_age,hue='Age Group',palette='rainbow')

"""From above Graph we can see that most of the buyers are of age group between 26-35 yrs female

**3. State**
"""

#total number of orders from top 10 states
sales_state = df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(x ='State',y='Orders',data=sales_state,hue='State',palette='rainbow')

#total number of Amount/sales from top 10 states
sales_state = df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(x ='State',y='Amount',data=sales_state,hue='State',palette='rainbow')

"""From above graph we can see that most of the orders & sales/amount are from Uttar Pradesh , Maharastra , karnataka respectively.

**4. Marital Status**
"""

ax=sns.countplot(x='Marital_Status',data=df,hue='Marital_Status')

sns.set(rc={'figure.figsize':(6,3)})
for bars in ax.containers:
    ax.bar_label(bars)

sales_ms = df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(x ='Marital_Status',y='Amount',data=sales_ms,hue='Gender')

"""From the above graph we can see that most of the buyers are married women and they have high purchasing power.

**5. Occupation**
"""

ax=sns.countplot(x='Occupation',data=df,hue='Occupation')

sns.set(rc={'figure.figsize':(20,5)})
for bars in ax.containers:
    ax.bar_label(bars)

sales_occupation = df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(x ='Occupation',y='Amount',data=sales_occupation,hue='Occupation')

"""From above graph we can see that most of the buyers are wokring in IT, Healthcare and Aviation sector.

**6. Product category**
"""

ax=sns.countplot(x='Product_Category',data=df,hue='Product_Category')

sns.set(rc={'figure.figsize':(30,5)})
for bars in ax.containers:
    ax.bar_label(bars)

sales_pcategory = df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x ='Product_Category',y='Amount',data=sales_pcategory,hue='Product_Category')

"""From above graph we can see that most selling products are Food, Clothing and Electronics category."""

sales_pid = df.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x ='Product_ID',y='Orders',data=sales_pid,hue='Product_ID')

"""**Conclusion :**

Married women age group 26-35 from UP, Maharastra and karnataka wokring in IT, Healthcare and Aviation are more likely to buy proudcts from Food, Clohting and Electronics category.
"""