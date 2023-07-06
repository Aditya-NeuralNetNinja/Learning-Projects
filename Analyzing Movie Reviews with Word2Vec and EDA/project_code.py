## Import required libraries

    import numpy as np # For linear algebra
    import pandas as pd # For data processing, CSV file I/O
    import os
    import matplotlib.pyplot as plt
    import seaborn as sns
    from gensim.models import Word2Vec
    from gensim.utils import simple_preprocess
    from sklearn.feature_extraction.text import CountVectorizer

## Load the data from csv file

    df = pd.read_csv("/kaggle/input/imdb-dataset-of-50k-movie-reviews/IMDB Dataset.csv")

## EDA

    print(df.describe()) # Summary statistics of the dataset

## Balanced dataset

    # Plotting the balance of the dataset for the label 'sentiment'
    df['sentiment'].value_counts().plot(kind='bar')
    plt.title('Distribution of Sentiments')
    plt.show()

    # Extracting the review column from the dataframe for our Word2Vec model
    cf = df["review"].apply(simple_preprocess) # Corpus file

    # To get a sense of the most common words, 
    #we can use a CountVectorizer to count words
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df['review'])
    word_counts = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

    # Plotting the most common words in reviews
    most_common_words = word_counts.sum().sort_values(ascending=False).head(10)
    most_common_words.plot(kind='barh')
    plt.title('Most Common Words in Reviews')
    plt.xlabel('Count')
    plt.ylabel('Words')
    plt.show()

## Model Building & Training

    # Instantiate a Word2Vec model with a specified minimum count & processors
    model = Word2Vec(cf, min_count=1, workers=4)

    # Build vocabulary from the input sequence of sentences (cf)
    model.build_vocab(cf)

    # Train Word2Vec model using the built vocabulary & default number of epochs
    model.train(cf, total_examples=model.corpus_count, epochs=model.epochs)

    # Saving the model
    model.save("/kaggle/working/name.model")

## Vocabulary

    # Checking output after applying simple_preprocess & building vocab
    print(model.wv.index_to_key[400:500]) # Show only 100 words in vocabulary

    # To get the word vector for a particular word
    print(model.wv.get_vector('movie'))

    # Print number of epochs and corpus count for the trained model
    print(f"Epochs: {model.epochs}, Corpus Count: {model.corpus_count}")

    # Finding most similar words to a given word
    print(model.wv.most_similar("cinematography"))

    # Finding similarity between two words
    print(model.wv.similarity("screenplay","director"))

    # Finding odd word
    print(model.wv.doesnt_match(["cinematography", "screenplay", "director", "actor"]))

    # Find word that is most similar to words in positive list &
    # most dissimilar from words in negative list
    print(model.wv.most_similar(positive=['actor','screenplay'], negative=['director']))

