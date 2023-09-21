import sys
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
# Assuming X is a DataFrame with features and Y is a Series with the target variable
df=pd.read_csv('test.csv')


# Preprocess data, handle missing values, encode categorical variables, etc.
X=df[['textID', 'text']]

X=X.drop(['textID'],axis=1)
X=X.dropna()
Y=df['sentiment']
Y=Y.dropna()
# print(Y.idxmax,'*'*100)

def mappingfunction(mapper,data,colname):
    for i in range(len(data[colname])):
        data[colname][i]=mapper[data[colname][i]]
    return data
def mappingseries(mapper,data):
    for i in range(len(data)):
        data[i]=mapper[data[i]]
    return data



# TF-IDF Transformation
vectorizer = TfidfVectorizer(max_features=5000)  # Limit the number of features (words)
X_text_tfidf = vectorizer.fit_transform(X['text'])
X_text_tfidf_df = pd.DataFrame(X_text_tfidf.toarray(), columns=vectorizer.get_feature_names_out())

# Drop the original 'text' column and concatenate the TF-IDF features
X = X.drop(['text'], axis=1)
X = pd.concat([X, X_text_tfidf_df], axis=1)


Ymap={'neutral':1,'negative':0,'positive':2}
Y=Y.map(Ymap)



# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)



model = LogisticRegression(multi_class='auto', solver='liblinear')


model.fit(X_train, y_train)

# Predict on the testing set
y_pred = model.predict(X_test)
y_pred2 = model.predict(X_train)
# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
# print("Testing Accuracy:", accuracy)
accuracy2 = accuracy_score(y_train, y_pred2)
# print("Training Accuracy2:", accuracy2)
# print(X_test)



# my_text = "I Love coding because I always want to code code code"

def process_text(input_text):
    # Your NLP processing logic here
    df=pd.read_csv('test.csv')


# Preprocess data, handle missing values, encode categorical variables, etc.
    X=df[['textID', 'text']]

    X=X.drop(['textID'],axis=1)
    X=X.dropna()
    Y=df['sentiment']
    Y=Y.dropna()
# print(Y.idxmax,'*'*100)



# TF-IDF Transformation
    vectorizer = TfidfVectorizer(max_features=5000)  # Limit the number of features (words)
    X_text_tfidf = vectorizer.fit_transform(X['text'])
    X_text_tfidf_df = pd.DataFrame(X_text_tfidf.toarray(), columns=vectorizer.get_feature_names_out())

# Drop the original 'text' column and concatenate the TF-IDF features
    X = X.drop(['text'], axis=1)
    X = pd.concat([X, X_text_tfidf_df], axis=1)


    Ymap={'neutral':1,'negative':0,'positive':2}
    Y=Y.map(Ymap)



# Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)



    model = LogisticRegression(multi_class='auto', solver='liblinear')


    model.fit(X_train, y_train)

# Predict on the testing set
    y_pred = model.predict(X_test)
    y_pred2 = model.predict(X_train)
# Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
# print("Testing Accuracy:", accuracy)
    accuracy2 = accuracy_score(y_train, y_pred2)
# print("Training Accuracy2:", accuracy2)
# print(X_test)
    if len(sys.argv) < 2:
        print("Usage: python nlpprogram.py <input_text>")

    my_text = sys.argv[1]
    my_text_tfidf = vectorizer.transform([my_text])
    my_text_tfidf_df = pd.DataFrame(my_text_tfidf.toarray(), columns=vectorizer.get_feature_names_out())
    predicted_sentiment = model.predict(my_text_tfidf_df)
    print("Your input text: "+my_text)
    if(predicted_sentiment==2):
        result = f"Positive Text"
    elif(predicted_sentiment==1):
        result = f"Neutral Text"
    elif(predicted_sentiment==0):
        result = f"Negative Text"
    processed_text = f"You submitted: {input_text} \n Result: {result}"
    return processed_text
    