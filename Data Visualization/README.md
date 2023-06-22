# Data Visualization of Ford's Car Dataset 🚗💰

This is a repository of an exploratory data analysis of a dataset related to Ford car prices. It also presents some useful insights and visualizations related to the car market. 📊✨

## 📚 Libraries Used 

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import style
style.use('seaborn')
```

## 🚀 Getting Started

The data used for this analysis is loaded from a CSV file.

```python
df = pd.read_csv('/kaggle/input/ford-car-price-prediction/ford.csv')
```

## 🧐 Exploratory Data Analysis (EDA)

The first steps in the analysis involve exploring the dataset, checking its head, info, checking for null values, and examining some basic statistical descriptions of the data.

```python
df.head()
df.info()
df.isnull().sum()
df.describe()
df.columns
```

## 📈 Data Visualization 

The dataset is visualized using various types of plots to understand the distribution and relationship of different features. This includes count plots, pie charts, bar plots, box plots, histograms, scatter plots, and a correlation heatmap.

```python
sns.countplot(x='transmission', data=df)
sns.countplot(y='fuelType', data=df)
df['year'].hist()
sns.displot(df.price)
sns.scatterplot(x=df['mpg'], y=df['price'], hue=df['fuelType'])
sns.heatmap(df.corr(), annot=True)
...
```

## 🔎 Inferences

From the exploratory analysis and visualization, we make several inferences about the dataset and features affecting car prices. These inferences help in understanding the data better and can guide subsequent steps of a data analysis or machine learning pipeline.

For instance, one of the inferences we made is:

1. Hybrid cars are majorly better in terms of fuel economy than other cars.
2. Many Diesel cars in price range $10k - 25k have better fuel economy than petrol cars.
3. Between fuel economy range 25-50, price range of diesel cars is more than petrol cars.

## 🔄 Data Preprocessing

Data preprocessing is an important step to prepare the data for any subsequent modeling. In this case, the 'transmission' and 'fuelType' features are converted to numeric using a mapping, and the 'model' column is dropped.

```python
df.replace({'transmission':{'Manual':0, 'Automatic':1, 'Semi-Auto':2}}, inplace=True)
df.replace({'fuelType':{'Petrol':0, 'Diesel':1, 'Hybrid':2, 'Electric':3, 'Other':4}}, inplace=True)
modified_df = df.drop("model", axis=1)
```

## Contact 📧🤝

For any queries related to this project, feel free to reach out at https://www.linkedin.com/in/aditya-chourasiya/ or raise an issue in the GitHub repository. 📬📊🤝

