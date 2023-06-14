# KMeans Clustering Project :chart_with_upwards_trend:

This project is an implementation of KMeans Clustering on a dataset containing information about individuals' age and income. The goal is to group individuals into clusters based on these two features. After using the elbow method to determine the optimal number of clusters, we have selected 3 as the optimal number of clusters.

## :file_folder: Dataset

The dataset used in this project is `income.csv` which contains the following columns:

- `Name`: The name of the individual.
- `Age`: The age of the individual.
- `Income($)`: The income of the individual.

## :hammer_and_wrench: Requirements

- Python 3.10
- pandas
- sklearn
- matplotlib

## :gear: Setup & Installation

```bash
pip install pandas sklearn matplotlib
```
:computer: Code
The code for this project is divided into several sections:

1. Imports: Importing the necessary libraries.
2. Loading the data: Loading the dataset using pandas.
3. Plotting the initial distribution of Age and Income: Visualizing the initial distribution of data.
4. Clustering: Using KMeans to cluster the data into 3 clusters.
5. Scaling the Age and Income attributes: Using MinMaxScaler to scale the Age and Income attributes.
6. Clustering again after scaling: Running KMeans again after scaling the attributes.
7. Finding the optimal number of clusters via the elbow method: Using the elbow method to find the optimal number of clusters.

## :bar_chart: Visualizations

The project includes several visualizations to better understand the data and the results of the clustering:

1. **Initial distribution of Age and Income**: A scatter plot showing the distribution of Age and Income before clustering.
![p1](https://github.com/Aditya-NeuralNetNinja/Learning-Projects/assets/108260519/e94c615c-8d7f-445c-95b3-bcb288408913)
   
2. **Clusters before scaling**: A scatter plot showing the clusters formed by KMeans before scaling the attributes.
![p2](https://github.com/Aditya-NeuralNetNinja/Learning-Projects/assets/108260519/5abafb41-0a3c-4317-8b73-264f79a087cd)

3. **Clusters after scaling**: A scatter plot showing the clusters formed by KMeans after scaling the attributes.
![p3](https://github.com/Aditya-NeuralNetNinja/Learning-Projects/assets/108260519/c599da3e-f4d5-4423-b229-19654d6e3c9a)

4. **Elbow method**: A line plot showing the sum of squared errors for different numbers of clusters, used to determine the optimal number of clusters.
![p4](https://github.com/Aditya-NeuralNetNinja/Learning-Projects/assets/108260519/0ec0a389-95c0-4364-84ed-d245824dd9dd)

## :mailbox_with_mail: Contact

For any queries, reach out to me at - https://www.linkedin.com/in/aditya-chourasiya/
