import pandas as pd
import matplotlib.pyplot as plt
import spacy

nlp = spacy.load('en_core_web_sm')

#LOAD DataFrame
wordsInDF = pd.read_csv("static/Extracted_Emotions_VERB_ADJ_ADV.csv")

wordsArray = wordsInDF['Word'].unique()

emotionArray = ['sadness', 'anger', 'love', 'surprise', 'fear', 'happy']

# LOADING FROM Emotion_Encoded
wordsInDF = pd.read_csv("static/Encoded_VERB_ADJ_ADV.csv")

wordsInDF = wordsInDF.drop('Unnamed: 0', axis=1)

# USING DECISION TREE TO MAKE PREDICTION
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
#TRAIN
model.fit(wordsInDF.drop("Emotion", axis = 1), wordsInDF.drop("Word", axis = 1))