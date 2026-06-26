
import pandas as pd
# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("understanding dataset")

file_name= 'sales_data.csv'
if not os.path.exists(file_name):
    print(f"error:{file_name} is not found")
    exit()

df=pd.read_csv('sales_data.csv')
print("succesfully loaded")
print(f"shape of the dataset is:{df.shape[0]},columns:{df.shape[1]}")
print(df.head())
print(df.tail())
print(df.describe())

print("Handling missing values")
print(df.isnull().sum())

median_age=df['Age'].median()
df['Age']=df['Age'].fillna(median_age)
print(median_age)
print(df.isnull().sum())

plt.figure(figsize=(7,4))
df['Spending'].hist(bins=10,color='skyblue',edgecolor='black')
plt.title('Distribution of pending')
plt.xlabel('Spending amount')
plt.ylabel('number of customers')
plt.show()

#boxplot
plt.figure(figsize=(10,5))
sns.boxplot(x=df['Spending'],color='yellow')
plt.title('boxplot of spending')
plt.xlabel('Spending amount')
plt.ylabel('number of customers')
plt.show()

Q1 = df["Age"].quantile(0.25)
Q3 = df["Age"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[(df["Age"] < lower) | (df["Age"] > upper)]
print(outliers)

#scatterplot
plt.figure(figsize=(7,4))
sns.scatterplot(x=df['Age'],y=df['Spending'])
plt.title('Scatter plot of Age vs Spending')
plt.xlabel('Age')
plt.ylabel('spending')
plt.show()

#correlation matrix
plt.figure(figsize=(10,5))
sns.heatmap(df.select_dtypes(include='number').corr(),annot=True,cmap='coolwarm',fmt='.2f')
plt.title('Correlation matrix of Age vs Spending')
plt.xlabel('spending amounts')
plt.ylabel('number of customers')
plt.show()


