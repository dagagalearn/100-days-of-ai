import tensorflow as tf
from tensorflow.keras import layers, models

(train_images,train_labels),(test_images,test_labels) = tf.keras.datasets.fashion_mnist.load_data()

train_images_mini = train_images[:1000]
train_labels_mini = train_labels[:1000]


overfit_model = models.Sequential([
    layers.Flatten(input_shape=(28,28)),
    layers.Dense(512,activation="relu"),
    layers.Dense(256,activation="relu"),
    layers.Dense(10, activation="softmax")
])

overfit_model.compile(optimizer="adam",loss="sparse_categorical_crossentropy",metrics=["accuracy"])
overfit_history = overfit_model.fit(train_images_mini,train_labels_mini,validation_data=(test_images,test_labels),epochs=50)

dropout_model = models.Sequential([
    layers.Flatten(input_shape=(28,28)),
    layers.Dense(512,activation="relu"),
    layers.Dropout(0.5),
    layers.Dense(256,activation="relu"),
    layers.Dropout(0.5),
    layers.Dense(10, activation="softmax")
])

dropout_model.compile(optimizer="adam",loss="sparse_categorical_crossentropy",metrics=["accuracy"])
dropout_history = dropout_model.fit(train_images_mini,train_labels_mini,validation_data=(test_images,test_labels),epochs=50)

import matplotlib.pyplot as plt
plt.subplot(1,2,1)
plt.plot(overfit_history.history["accuracy"], label="Train_no_dropout")
plt.plot(overfit_history.history["val_accuracy"], label="Val_no_dropout")
plt.legend()
plt.title("Without Dropout")
plt.grid(True)

plt.subplot(1,2,2)
plt.plot(dropout_history.history["accuracy"], label="Train_dropout")
plt.plot(dropout_history.history["val_accuracy"], label="Val_dropout")
plt.legend()
plt.title("With Dropout")
plt.grid(True)

plt.show()




