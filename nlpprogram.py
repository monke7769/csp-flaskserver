import sys
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import joblib

def process_text(input_text):
    
    if len(sys.argv) < 2:
        print("Usage: python nlpprogram.py <input_text>")
        
        
    # vectorizer = TfidfVectorizer(max_features=5000) #using bag of words to convert to an array
    model=joblib.load('emotionnlp.joblib') # importing the module back in
    vectorizer = joblib.load('tfidf_vectorizer.joblib')
    my_text = input_text
    
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
    