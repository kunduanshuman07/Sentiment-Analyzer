from flask import Flask, request, jsonify
from flask_cors import CORS
import utils

app = Flask(__name__)
CORS(app)

@app.route('/predict_sentiment', methods=['GET', 'POST'])
def predict_sentiment():
    data = request.get_json()
    sentiment = data.get('sentiment')
    prediction = utils.get_prediction(sentiment)
    return prediction

if __name__ == "__main__":
    print("Python server up and running")
    app.run(host='0.0.0.0', debug = True)
