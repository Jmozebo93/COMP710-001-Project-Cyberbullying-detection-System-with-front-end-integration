#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


# In[4]:


import re
import nltk
from nltk.util import pr
from nltk.stem import WordNetLemmatizer
#stemmer = nltk.SnowballStemmer("english")
from nltk.corpus import stopwords
import string 
#stopword = set(stopwords.words("english"))

# Download NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize NLTK components
stopword = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


# In[5]:


df = pd.read_csv("/workspaces/COMP710-001-Project-Cyberbullying-detection-System-with-front-end-integration/Dataset/twitter_parsed_dataset.csv")
#print(df.head())
#print(df.isnull().sum())
# Handle NaN values
df.dropna(inplace=True)  # Drop rows with NaN values


# In[6]:


#df['oh_label'] = df['Annotation'].map({0.0:"Not racism or sexism", 1.0:"racism or sexism"})
#df['labels'].fillna("No hate or offensive speech", inplace=True)
# Drop rows with NaN values in the 'labels' column
#df.dropna(subset=['labels'], inplace=True)
#print(df.head())


# In[7]:


df = df[['Text', 'Annotation']]
#print(df.head())


# In[8]:


def clean(text):
    
    #convert text to lower case
    text = str(text).lower()
    
    # Remove URLs, HTML tags, special characters, and digits
    text = re.sub(r'http\S+|www\S+|<.*?>|[^a-zA-Z\s]', '', text)
    
    #Remove squared brackets and their contents
    #text = re.sub('\[.*?\]', '', text)
    
    #Remove URLs (http/https) and website links (www)
    #text = re.sub('https?://\S+|www\.\S+', '', text)
    
    #Remove HTML tags
    #text = re.sub('<.*?>+', '', text)
    #Remove percentage sign
    #text = re.sub('[%]','',text)
  
    #text = re.sub('\n', '', text)
    
    #Remove words containing digits
    #text = re.sub('\w*\d\w*', '', text)
    
    # Remove exclamation points, "@" symbols, and colons
    #text = re.sub(r'[!@:]', '', text)
    
    #Tokenize the text and remove stopwords
    #text = [word for word in text.split(' ') if word not in stopword]
    
    # Tokenize and remove stopwords
    tokens = [word for word in text.split() if word not in stopword]
    
    # Lemmatize tokens
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    #Join the cleaned words back into a string
    #text = " ".join(text)
    
    #text = [stemmer.stem(word) for word in text.split(' ')]
    
    #text = " ".join(text)
    
    #return text
    return ' '.join(tokens)

df["Text"] = df["Text"].apply(clean)
#print(df.head())


# In[9]:


x = np.array(df["Text"])
y = np.array(df["Annotation"])

X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state= 42)

#cv = CountVectorizer()
# Feature extraction using TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)  # Limit features to top 5000
#x = cv.fit_transform(x)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)


# Initialize Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier
clf.fit(X_train_tfidf, y_train)

#clf = DecisionTreeClassifier()

#clf.fit(X_train, y_train)


# In[10]:


#Make predictions on the testing data
y_pred = clf.predict(X_test_tfidf)
#y_pred = model.predict_classes(X_test_pad)


# In[11]:


#Evaluate the performance of the classifier
accuracy = accuracy_score(y_test, y_pred)

#print("Accuracy: ", accuracy*100)


# In[12]:


#print("Classification Report:")
#print(classification_report(y_test, y_pred))


# In[13]:


#print("Confusion Matrix:")
#print(confusion_matrix(y_test, y_pred))


# In[14]:


test_data = "I'm not sexist but women should not be working"

# Apply the same preprocessing steps to the test data
clean_test_data = clean(test_data)

# Transform the preprocessed test data using the same vectorizer used for training data
test_data_vectorized = vectorizer.transform([clean_test_data]).toarray()

# Make predictions on the test data
predicted_label = clf.predict(test_data_vectorized)





# In[15]:


# Check if the predicted label is "racism" or "sexism"
if predicted_label in ["racism", "sexism"]:
    print("Cyberbullying")
else:
    print(predicted_label)

