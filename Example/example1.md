from flask import Flask, request
import calcuap

app = Flask(__name__)

@app.route('/integration', methods=['POST'])
def integration():
    json = request.get_json()
    function = json["function"]
    lower = json["lower"]
    upper = json["upper"]
    result = calcuap.integration(function, lower, upper)
    return f'The definite integral of the function from {lower} to {upper} is: {result}'

@app.route('/differentiation', methods=['POST'])
def differentiation():
    json = request.get_json()
    function = json["function"]
    point = json["point"]
    result = calcuap.differentiation(function, point)
    return f'The derivative of the function at {point} is: {result}'

if __name__ == '__main__':
    app.run(debug=True)
