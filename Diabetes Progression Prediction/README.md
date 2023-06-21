# 🩺 Diabetes Progression Prediction 📊

This project involves the use of the built-in diabetes dataset from `sklearn.datasets` for predicting diabetes progression. The goal is to predict a quantitative measure of disease progression one year after baseline, which is a continuous variable, with higher values indicating more severe disease progression.

## 📂 Repository Contents
The repository consists of two main files:

1. `Code.py` - The Python script encapsulating the implementation of various regression models. 

2. `diabetes_regression_models.ipynb` - A Jupyter Notebook comprising executed code, inclusive of all the model outputs.

## 📚 Data Used
The data for the project was obtained from the built-in diabetes dataset provided by `sklearn.datasets`. This dataset features ten baseline variables such as age, sex, body mass index, average blood pressure, and six blood serum measurements, gathered from 442 diabetes patients.

## 🧪 Models Explored
Several regression models were explored during the project, including:

- Linear Regression
- Stochastic Gradient Descent (SGD) Regressor
- Decision Tree Regressor
- Random Forest Regressor
- K-Nearest Neighbors (KNN) Regressor
- Polynomial Regression with Random Forest Regressor

The models were evaluated using standard regression metrics such as the R-squared score, Mean Squared Error (MSE), and Mean Absolute Error (MAE).

## 🏆 Final Model Selected
The model that demonstrated superior performance was the Random Forest model with Polynomial Features. It achieved an R2 score of approximately 0.523, accounting for about 52.3% of the variance in the disease progression. Moreover, it had the lowest mean absolute error, indicating that its predictions, on average, were closer to the actual values.

## 🚀 Getting Started
To set up this project on your local machine, follow the instructions below:

## 🔑 Prerequisites
The software required to run the program includes:
- Python 3.x
- Jupyter Notebook
- Scikit-learn

## 🔧 Installation
Clone the repository to your local machine:
   ```sh
   git clone https://github.com/Aditya-NeuralNetNinja/Diabetes-Progression-Prediction.git
   ```

## 📊 Running the Tests
For each model, you can run the scripts provided in the Jupyter notebook, which incorporate all the necessary steps, from loading the data to evaluating the models.

## 🧰 Built With
The project utilizes the following frameworks, libraries, and modules:
- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Scikit-Learn](https://scikit-learn.org/)

## 💼 Contributing
Contributions to this project are welcome! Fork the repo and create a Pull Request with your changes. We would be happy to review and include your contributions.

## 📬 Contact
LinkedIn: [Aditya Chourasiya](https://www.linkedin.com/in/aditya-chourasiya/)

Email: adityachrs7@gmail.com
