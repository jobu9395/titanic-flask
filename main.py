# Local imports
import datetime

# Third part imports
from flask import Flask, request
import pandas as pd
import joblib


model_name = "Titanic survivability machine learning model"
model_file = 'model.pkl'
version = "v1.0.0"


def get_model_response(json_data):
    X = pd.DataFrame.from_dict(json_data)
    prediction = clf.predict(X)[0]
    if prediction == 1:
        label = "A person with these stats would have survived"
    else:
        label = "A person with these stats would have died"
    return {
        'status': 200,
        'label': label,
        'prediction': int(prediction)
    }

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def info():
    """Return model information, version, how to call"""
    result = {}

    result["name"] = model_name
    result["version"] = version

    return result


@app.route('/health', methods=['GET'])
def health():
    """Return service health"""
    return 'ok'


@app.route('/predict', methods=['POST'])
def predict():
    feature_dict = request.get_json()
    if not feature_dict:
        return {
            'error': 'Body is empty.'
        }, 500

    try:
        response = get_model_response(feature_dict)
    except ValueError as e:
        return {'error': str(e).split('\n')[-1].strip()}, 500

    return response, 200


if __name__ == '__main__':
    clf = joblib.load('model.pkl')
    app.run(debug=True)