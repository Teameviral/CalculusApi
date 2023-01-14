# Import necessary modules
import tensorflow as tf
from tensorflow import keras
import numpy as np

# Load the dataset
(x_train, y_train), (x_test, y_test) = keras.datasets.boston_housing.load_data()

# Scale the input data
x_train = keras.utils.normalize(x_train)
x_test = keras.utils.normalize(x_test)

# Define the model
model = keras.Sequential()
model.add(keras.layers.Dense(13, input_shape=(13,), activation='relu'))
model.add(keras.layers.Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(x_train, y_train, epochs=100)

# Evaluate the model
test_loss = model.evaluate(x_test, y_test)
print('Test loss:', test_loss)

# Save the model
model.save('model.h5')
