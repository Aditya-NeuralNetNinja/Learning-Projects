# :clapper: Analyzing Movie Reviews with Word2Vec and EDA :mag:

This project is an in-depth analysis of a large dataset of movie reviews using natural language processing (NLP), specifically using the Word2Vec algorithm from the Gensim library, and Exploratory Data Analysis (EDA) methods. The data comprises 50,000 IMDB movie reviews, which we clean, preprocess, and then use to train a Word2Vec model. We also visualize the frequency of words in the reviews and the distribution of sentiments. The outcome is a model that can generate similar words for any given word from the reviews, providing fascinating insights into movie review content.

## :rocket: Getting Started

To get started with this project, the following libraries need to be installed:

- `numpy`: For performing numerical operations.
- `pandas`: Used for data manipulation and analysis.
- `matplotlib`: A plotting library to create static, animated, and interactive visualizations in Python.
- `seaborn`: Based on matplotlib, it provides a high-level interface for drawing attractive and informative statistical graphics.
- `gensim`: A robust open-source vector space modeling and topic modeling toolkit.
- `sklearn`: A machine learning library for Python, featuring various classification, regression, and clustering algorithms.

## :file_folder: Dataset

The dataset used in this project is the IMDB Dataset of 50K Movie Reviews. You can download it from [this link](https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews).

## :gear: Project Structure

The project is structured in the following way:

1. **Importing required libraries:** Essential Python libraries for data processing, visualization, and NLP are imported.

2. **Loading the data:** The IMDB movie reviews dataset is loaded into a Pandas DataFrame.

3. **Exploratory Data Analysis (EDA):** Basic EDA is performed on the dataset. We visualize the distribution of sentiments and the most common words in the reviews.

4. **Data preprocessing:** The review text data is cleaned and preprocessed using `simple_preprocess` from the Gensim library.

5. **Model Building:** A Word2Vec model is built and trained on the preprocessed data.

6. **Exploring the Model:** The trained model is then explored by visualizing the vocabulary and finding similar words for a given word.

## :eyes: Results

Using this project, you can explore the distribution of sentiments and the most frequent words in the dataset. Additionally, the trained Word2Vec model can give you the closest words for any given word in the context of movie reviews.

## :memo: Note

This project is a great starting point for anyone interested in NLP, and wants to understand it via a practical example.

## :trophy: Conclusion

Analyzing and visualizing large text datasets can be challenging, but with the right tools and techniques, it becomes a lot more manageable and fun. This project gives you a hands-on example of how to approach such a task.

Feel free to explore, learn and improve! :sparkles:

## :handshake: Contributing

Contributions, issues, and feature requests are welcome!

## :email: Contact

Reach out to me for any project queries, mentoring requests, or collaboration proposals. Connect with me on LinkedIn [here](https://www.linkedin.com/in/aditya-chourasiya/) or drop me an email at adityachrs7@gmail.com. Always happy to help and collaborate! :grinning:
