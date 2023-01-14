# CalculusApi

This code defines a Flask application that serves as an API for performing integration and differentiation. The API has two endpoints, /integration and /differentiation, that can be accessed using a POST request.

The integration endpoint expects a JSON object in the request body with the following properties:

function1: a string representing the mathematical function to be integrated
lower: a numeric value representing the lower bound of the integration
upper: a numeric value representing the upper bound of the integration
The differentiation endpoint expects a JSON object in the request body with the following properties:

function2: a string representing the mathematical function to be differentiated
point: a numeric value representing the point at which the derivative should be calculated
Both endpoints use a pre-trained model, which is loaded at the beginning of the script using the keras.models.load_model function. The model is expected to be saved in a file named model.h5 in the same directory as the script.

The integration and differentiation functions use the predict method of the model to obtain the definite integral and derivative of a function. They then return the result in the form of a string, which is the response of the API.

The script starts the Flask application if the script is run as the main module.

You need to make sure that your dataset and model are trained properly and saved in "model.h5" at the same directory of the script. Also, you need to check that the dataset of your trained model corresponds to the input data of the integration and differentiation endpoints of the API.
