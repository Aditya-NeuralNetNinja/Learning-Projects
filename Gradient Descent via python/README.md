# Gradient Descent Implementation in Python 📈🔎🐍

This repository contains the Python implementation of Gradient Descent, a simple yet powerful optimization algorithm widely used in machine learning and deep learning. 🔍📉🔬

![AngryInconsequentialDiplodocus-size_restricted](https://github.com/Aditya-NeuralNetNinja/Learning-Projects/assets/108260519/3af86e57-59a7-47eb-a352-410d86beb383)


## Overview 📚🔍

The code in this repository is a simple implementation of Gradient Descent. Gradient Descent is a first-order iterative optimization algorithm for finding the minimum of a function. Here, we use it to find parameters `w` (weight) and `b` (bias) for a linear regression problem, where our goal is to find a line that best fits a set of points. 📉🧪🔎

## Repository Files 📁📂

The repository contains the following file:

- `gradient_descent.py`: This is the main Python script containing the implementation of Gradient Descent. 🐍📝

## Code Details 💻📋

### Variables 📊🔢

- `x`: A numpy array of shape (10,1) with random values.
- `y`: Our target variable. It's a linear transformation of `x` with some random noise.
- `w` and `b`: Parameters we are trying to optimize using Gradient Descent.
- `learning_rate`: The learning rate for the Gradient Descent. 📈🔬

### Function: `descent(x,y,w,b,learning_rate)` ⚙️🔄

This function implements one step of the Gradient Descent.

- Inputs:
  - `x`: A numpy array representing our feature.
  - `y`: A numpy array representing our target.
  - `w` and `b`: Current estimates of the parameters.
  - `learning_rate`: The learning rate for the Gradient Descent.
- Outputs:
  - Updated estimates of `w` and `b`.

The function uses the Mean Squared Error (MSE) loss. The gradients of the loss function with respect to `w` and `b` are calculated and used to update the values of `w` and `b`. 🧪📈📉

### Main Loop 🔄🔁

The Gradient Descent is run iteratively for a pre-defined number of epochs (here, 400). After each epoch, we print the current loss and the updated values of `w` and `b`. 🔁📉🔍

At the end of the script, the final values of `x` and `y` are printed out.

## Usage 🚀📌

To run the code, ensure that Python and numpy are installed in your environment.

```
python gradient_descent.py
```

## Dependencies 📦🔗

- [Python](https://www.python.org/)
- [NumPy](https://numpy.org/)

## Contact 📧📞

While this is a simple project and not accepting contributions, if you have any questions, please feel free to reach out - https://www.linkedin.com/in/aditya-chourasiya/ 🤝💬
