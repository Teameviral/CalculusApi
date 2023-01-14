# CalculusApi

This code defines a Flask application that serves as an API for performing integration and differentiation. The API has two endpoints, `/integration` and `/differentiation`, that can be accessed using a POST request.

The integration endpoint expects a JSON object in the request body with the following properties:

+function1: a string representing the mathematical function to be integrated
lower: a numeric value representing the lower bound of the integration
upper: a numeric value representing the upper bound of the integration
The differentiation endpoint expects a JSON object in the request body with the following properties:

-function2: a string representing the mathematical function to be differentiated
point: a numeric value representing the point at which the derivative should be calculated
Both endpoints use a pre-trained model, which is loaded at the beginning of the script using the keras.models.load_model function. The model is expected to be saved in a file named model.h5 in the same directory as the script.

The integration and differentiation functions use the predict method of the model to obtain the definite integral and derivative of a function. They then return the result in the form of a string, which is the response of the API.

The script starts the Flask application if the script is run as the main module.

You need to make sure that your dataset and model are trained properly and saved in "model.h5" at the same directory of the script. Also, you need to check that the dataset of your trained model corresponds to the input data of the integration and differentiation endpoints of the API.

# Model Scripts

This script is a basic example of how to train a model using TensorFlow and the Keras API. Here's an overview of what the script does:

Imports necessary modules: The script imports TensorFlow, the Keras API, and Numpy.

Load the dataset: The script uses the built-in Boston Housing dataset, which is included in the Keras library. It loads the dataset into training and testing sets.

Scale the input data: The script normalizes the input data by dividing each value by the maximum value in the dataset. This is done to ensure that all the input data is in the same range and helps with the training process.

Define the model: The script creates a Sequential model and adds two Dense layers to the model. The first layer has 13 neurons and the second has 1 neuron. The first layer is the input layer and the second is the output layer.

Compile the model: The script compiles the model by specifying the optimizer (Adam) and the loss function (mean squared error)

Train the model: The script trains the model using the x_train and y_train data, and runs it for 100 epochs

Evaluate the model: The script evaluates the model by using the x_test and y_test data and prints the test loss.

Save the model: The script saves the trained model to a file named "model.h5"

This script is a basic example of how to train a model using the Boston Housing dataset and it is not related to integration and differentiation. In order to train a model that can handle integration and differentiation, you will need a more comprehensive dataset and also need to handle the symbolic math expressions and also need to integrate the model with the flask API.


