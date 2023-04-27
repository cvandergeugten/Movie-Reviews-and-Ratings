# Movie-Reviews-and-Ratings
Simple NLP analysis on text reviews

The goal of this project was to obtain real-world text data from a website and then analyze the text data to make predictions about a particular variable in the dataset. In this case, the data was obtained from https://www.rottentomatoes.com/ and contains the Movie Title, Movie Rating, and Movie Review (text). The ratings and reviews were written and submitted by common users (not professional critics). Reviews were scraped from 100+ different movies so that we can get a wide variety of review content. This dataset has also been posted on https://www.kaggle.com/datasets/chancev/movie-reviews-and-ratings so that Kaggle user's can download the data and use it for their own analysis and practice.

Contents of this repository:

* Python script used the scrape the data
* CSV file created by the python script (our dataset)
* Jupyter notebook with a simple NLP analysis predicting a user's rating based on their text review

This project aimed to perform simple natural language processing (NLP) on movie reviews using Python's pandas and nltk libraries. After loading a dataset of movie reviews, which contained the movie title, rating, and review text, the data was cleaned by removing rows with null values. The ratings were then transformed into binary variables (bad or good) using a threshold of 2.5, and the distribution of the ratings was visualized with a pie chart. The preprocessing stage involved removing all punctuation and stopwords from the review text.

Next, several machine learning models were trained and tested to classify the reviews based on their binary rating type. First, a multinomial naive Bayes (NB) model was used. The reviews were tokenized using the count vectorizer and transformed into weighted TF-IDF scores before being fed into the NB classifier. The precision and recall of this model were 1.0 and 0.02, respectively, for the 'bad' rating and 0.71 and 1.0, respectively, for the 'good' rating. The accuracy of this model was 0.71, with a macro-average F1 score of 0.43.

Next, a basic decision tree model was trained on the preprocessed review text. This model achieved an accuracy of 0.76, with a macro-average F1 score of 0.61. However, the precision and recall for the 'bad' rating were only 0.44 and 0.45, respectively, indicating a lower performance in correctly classifying negative reviews. Overall, the project provided an overview of the process of cleaning and processing text data and using it to train machine learning models for classification tasks.

Note that the output of the code is provided in the project, showing the confusion matrix and classification report for each model.
