from flask import Flask, request
from tensorflow import keras
import numpy as np

app = Flask(__name__)

# Loading the saved model
model = keras.models.load_model('model.h5')

@app.route('/integration', methods=['POST'])
def integration():
    # Getting the parameters passed in the request
    json = request.get_json()
    function = json["function"]
    lower = json["lower"]
    upper = json["upper"]
    # Predictive part
    result = model.predict(np.array([[function, lower, upper]]))
    return f'The definite integral of the function from {lower} to {upper} is: {result[0][0]}'

@app.route('/differentiation', methods=['POST'])
def differentiation():
    # Getting the parameters passed in the request
    json = request.get_json()
    function = json["function"]
    point = json["point"]
    # Predictive part
    result = model.predict(np.array([[function, point]]))
    return f'The derivative of the function at {point} is: {result[0][0]}'

if __name__ == 'main':
    app.run(debug=True)