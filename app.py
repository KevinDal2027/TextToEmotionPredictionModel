from flask import Flask, request, render_template, redirect, url_for
import matplotlib.pyplot as plt
from predictionModel import model
from predictionModel import wordsArray
from predictionModel import emotionArray
import spacy
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    test = request.form['user_text']
    testIndices = []
    test = test.lower()

    nlp = spacy.load('en_core_web_sm')
    test = nlp(test)

    for word in test:
        if word.text in list(wordsArray) and word.pos_ in ['VERB', "ADJ", "ADV", "NOUN"]:
            if word.pos_ == 'ADJ':
                testIndices.append(list(wordsArray).index(word.lemma_))
            testIndices.append(list(wordsArray).index(word.lemma_))
    testDF = pd.DataFrame({'Word': testIndices})

    if len(testIndices) <= 0:
        return render_template('result.html', labels=emotionArray, data=[0,0,0,0,0,0])

    emotionScalar = [0] * len(emotionArray)

    for i in model.predict(testDF):
        emotionScalar[i] += 1

    finalEmotionPieScalar = []
    finalEmotionPie = []
    for i in emotionScalar:
        if i > 0 and emotionArray[emotionScalar.index(i)] not in finalEmotionPie:
            finalEmotionPie.append(emotionArray[emotionScalar.index(i)])
            finalEmotionPieScalar.append(i)

    total = sum(finalEmotionPieScalar)
    finalEmotionPieScalarPercentage = [(count / total) * 100 for count in finalEmotionPieScalar]

    return render_template('result.html', labels=finalEmotionPie, data=finalEmotionPieScalarPercentage)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
