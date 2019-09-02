from flask import Flask, request, jsonify
from app import app

from joblib import load
import pandas as pd

model = load('models/model.joblib')
tfidf = load('models/tfidf.joblib')
id_to_category = load('models/id_to_category.joblib')


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/predict', methods=['POST'])
def predict():
    _json = request.json
    print(_json['data'])
    df = pd.DataFrame(_json['data'])

    predicted_codes = model.predict(tfidf.transform(df['description']))
    predicted_categories = [id_to_category[c] for c in predicted_codes]
    df['predicted_category'] = predicted_categories

    return df.to_json(orient='records')
