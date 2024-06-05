import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten
from keras.optimizers import Adam

from tensorflow.keras.datasets import mnist



(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train / 255
x_test = x_test / 255


y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

model = keras.models.Sequential([
    Flatten(input_shape=(28, 28, 1)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

print(model.summary())

model.compile(
    optimizer='adam',
    loss='cotegorical_crossentropy',
    metrics=['accuracy']
)

model.fit(x_train, y_train, batch_size=32, epochs=5, validation_split=0.2)
