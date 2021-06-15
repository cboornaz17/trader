#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import re
import nltk 
import matplotlib.pyplot as plt
#%matplotlib inline


# ### Importing the training set
# We will be importing a popular open source dataset of [airlines tweets & their sentiment analysis](https://raw.githubusercontent.com/kolaveridi/kaggle-Twitter-US-Airline-Sentiment-/master).
# 
# Below are some initial visualizations of the dataset.

# In[2]:


data_source_url = "https://raw.githubusercontent.com/kolaveridi/kaggle-Twitter-US-Airline-Sentiment-/master/Tweets.csv"
airline_tweets = pd.read_csv(data_source_url)


# In[3]:


airline_tweets.head()


# ### Initial Analysis
# Plot some details & stats about the dataset

# In[4]:


# Set up matplotlib settings
plot_size = plt.rcParams["figure.figsize"] 
print(plot_size[0]) 
print(plot_size[1])

plot_size[0] = 8
plot_size[1] = 6
plt.rcParams["figure.figsize"] = plot_size 


# In[5]:


airline_tweets.airline.value_counts().plot(kind='pie', autopct='%1.0f%%')


# In[6]:


print(len(airline_tweets))
print(airline_tweets.shape)
print(type(airline_tweets.airline_sentiment.value_counts()))
airline_tweets.airline_sentiment.value_counts()


# In[7]:



airline_tweets.airline_sentiment.value_counts().plot(kind='pie', autopct='%1.0f%%', colors=["red", "yellow", "green"])


# ### Importing the stock tweets to test
# Here we use our Twitter package to get sample tweets

# In[8]:


import os
import sys
from trader import TwitterController, TweetResponse

bearer=os.environ.get('BEARER_TOKEN')
twitter = TwitterController(bearer=bearer)

query = "GME"
maximum = 100

response = twitter.search_tweets(query, maximum)
try:
    print(len(response))
    #print('sample: ', response[:1])
    print(response[0].keys())
except Error:
    print('err in request')
    sys.exit(1)


sys.exit()
# In[9]:


# Get just the tweet text from the Twitter response
def get_tweet_text(response):
    print(response[0])
    isolate_tweets = np.vectorize(lambda obj: obj['text'])
    return isolate_tweets(np.array(response))


# In[10]:


# Get only the tweets value from the response dict
tweets = get_tweet_text(response)


# ### Clean the Data
# Extract the tweets and perform some basic parsing.

# In[11]:


def process_features(features):
    processed_features = []

    for sentence in range(0, len(features)):
        # Account for negative contractions
        processed_feature = re.sub(r'(\w+)n\'t', '\g<1> not', str(features[sentence]))
        
        # Remove all numbers
        processed_feature = re.sub('^\d+\s|\s\d+\s|\s\d+$', ' ', processed_feature)
        
        # Remove all the special characters
        processed_feature = re.sub(r'\W', ' ', processed_feature)

        # Remove all single characters
        processed_feature= re.sub(r'\s+[a-zA-Z]\s+', ' ', processed_feature)

        # Remove single characters from the start
        processed_feature = re.sub(r'\^[a-zA-Z]\s+', ' ', processed_feature) 

        # Substituting multiple spaces with single space
        processed_feature = re.sub(r'\s+', ' ', processed_feature, flags=re.I)

        # Removing prefixed 'b'
        processed_feature = re.sub(r'^b\s+', '', processed_feature)

        # Converting to Lowercase
        processed_feature = processed_feature.lower()

        processed_features.append(processed_feature)

    processed_features = np.array(processed_features)
    print('processed features sample: ', processed_features[:20])
    return processed_features


# In[12]:


features = airline_tweets.iloc[:, 10].values
labels = airline_tweets.iloc[:, 1].values
print("labels sample ", labels[:5])

sys.stdout.flush()
# In[13]:


processed_airline_features = process_features(features)


# In[14]:


processed_stock_features = process_features(tweets)


# ### Get the Vocabulary
# We want the unique set of words used in both the airline tweets and the stock tweets

# In[15]:


def get_unique_features_set(documents):
    s = set()
    for doc in documents:
        for word in doc.split(' '):
            if (len(word) != 0):
                s.add(word)
        
    print('got', len(s), 'unique words')
    return s

# Get the union set of unique words
stock_feature_names = get_unique_features_set(processed_stock_features)
airline_feature_names = get_unique_features_set(processed_airline_features)

total_unique_features = np.array(list(stock_feature_names.union(airline_feature_names)))
print('got',total_unique_features.shape,'total unique features!')


# ### Vectorize the text
# Here we use the TF-IDF method to parse the tweets into vectors of numbers.
# - [TF-IDF](https://monkeylearn.com/blog/what-is-tf-idf/)
# - [SciKitLearn TfIdfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)

# In[16]:


from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(max_features=2500, min_df=7, max_df=0.8, vocabulary=total_unique_features, stop_words=stopwords.words('english'))
processed_airline_features = vectorizer.fit_transform(processed_airline_features).toarray()


# ### Training the Model
# Here we use the same airline tweet dataset above to train a model for tweet sentiment analysis.

# In[17]:


from sklearn.model_selection import train_test_split

print('splitting into test set...')

# test_size .2 means we use 80% of the dataset to train the model
# and test it on the other 20%
X_train, X_test, y_train, y_test = train_test_split(processed_airline_features, labels, test_size=0.2, random_state=0)


# In[ ]:


from sklearn.ensemble import RandomForestClassifier

print('running randomForestClassifier')
text_classifier = RandomForestClassifier(n_estimators=200, random_state=0)
text_classifier.fit(X_train, y_train)


# In[ ]:


print(X_train.shape)
print(X_test.shape)
predictions = text_classifier.predict(X_test)


# In[ ]:


from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def printResults(y_test, predictions):
    print('confusion matrix\n')
    print(confusion_matrix(y_test,predictions))
    
    print('\nclassification report')
    print(classification_report(y_test,predictions))
    
    print('\naccuracy score')
    print(accuracy_score(y_test, predictions))
    
printResults(y_test, predictions)


# In[ ]:


# Vectorize the parsed tweets
stock_vectorizer = TfidfVectorizer(max_features=2500, min_df=.05, max_df=0.9, vocabulary=total_unique_features, stop_words=stopwords.words('english'))
processed_stock_features = stock_vectorizer.fit_transform(processed_stock_features).toarray()
print(processed_stock_features.shape)

predictions = text_classifier.predict(processed_stock_features)


# ### View the results!

# In[ ]:


# sanity checks
print(tweets.shape)
print(predictions.shape)


# In[ ]:


tweets = tweets.reshape((100,1))
predictions = predictions.reshape((100, 1))
print(tweets.shape)
print(predictions.shape)

total = np.concatenate((tweets, predictions), axis=1)
print(total.shape)

print(total)


# In[ ]:





# In[ ]:


predictions_df = pd.DataFrame(predictions)
predictions_df.value_counts().plot(kind='pie', autopct='%1.0f%%', colors=["red", "yellow", "green"])


# In[ ]:





# ### Todos
# 1. Move all logic into functions so we can test passing in our own data
# 1. Improve docs
# 1. Multithread training?
