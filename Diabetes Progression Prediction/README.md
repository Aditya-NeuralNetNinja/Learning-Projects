# 🩺 Diabetes Progression Prediction 📊

In this project, we've utilized the built-in diabetes dataset from `sklearn.datasets` to predict diabetes progression. This dataset includes ten baseline variables such as age, sex, body mass index, average blood pressure, and six blood serum measurements obtained from 442 diabetes patients. Our goal is to predict the quantitative measure of disease progression one year after baseline.

## 📂 Repository Contents
The repository includes two main files:

1. `Code.py` - The raw Python script that contains the implementation of various regression models. 

2. `diabetes_regression_models.ipynb` - The Jupyter Notebook file with the executed code, which includes all the model outputs and visual representations.

## 📚 Data Used
We're using the built-in diabetes dataset from `sklearn.datasets`. This dataset includes ten baseline variables, age, sex, body mass index, average blood pressure, and six blood serum measurements obtained from 442 diabetes patients.

The target variable is a quantitative measure of disease progression one year after baseline. It's a continuous variable, with higher values indicating more severe disease progression.

## 🧪 Models Explored
We've worked on various regression models, including:

- Linear Regression
- Stochastic Gradient Descent (SGD) Regressor
- Decision Tree Regressor
- Random Forest Regressor
- K-Nearest Neighbors (KNN) Regressor
- Polynomial Regression with Random Forest Regressor

Each model has been evaluated using standard regression metrics such as the R-squared score, Mean Squared Error (MSE), and Mean Absolute Error (MAE).

## 🏆 Final Model Selected
The Random Forest model with Polynomial Features was selected as the final model for its superior performance. This model achieved an R2 score of approximately 0.523, explaining about 52.3% of the variance in the disease progression. Additionally, it has the lowest mean absolute error, indicating that, on average, its predictions are closer to the actual values.

## 🚀 Getting Started
To get a local copy up and running, follow these simple steps.

## 🔑 Prerequisites
This is a list of software you need to have in order to run the program.
- Python 3.x
- Jupyter Notebook
- Scikit-learn

## 🔧 Installation
To set up this project on your local machine, please follow the instructions below:

Clone the repository to your local machine:
   ```sh
   git clone https://github.com/Aditya-NeuralNetNinja/Diabetes-Progression-Prediction.git


## 📊 Running the Tests
For each model, you can run the provided scripts in the Jupyter notebook, which include all the necessary steps, from loading the data to evaluating the models.

## 🧰 Built With
This project was built with the following frameworks, libraries, and modules:
- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Scikit-Learn](https://scikit-learn.org/)

## 💼 Contributing
If you would like to contribute to this project, please feel free to fork the repo and create a Pull Request with your changes. We would love to review and include your contributions.

## 📬 Contact
LinkedIn: [Aditya Chourasiya](https://www.linkedin.com/in/aditya-chourasiya/)
Email: adityachrs7@gmail.com
