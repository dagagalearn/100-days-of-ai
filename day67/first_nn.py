import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

(train_images, train_labels),(test_images,test_labels) = keras.datasets.fashion_mnist.load_data()
train_images = train_images/255
test_images = test_images/255
plt.imshow(train_images[100],cmap="gray")
plt.colorbar()
plt.show()

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128,activation="relu"),
    keras.layers.Dense(10,activation="softmax")
])

model.compile(
    optimizer = "adam",
    loss = "sparse_categorical_crossentropy",
    metrics = ['accuracy']
)

model.fit(train_images, train_labels,epochs=11)

loss_score, accuracy_score = model.evaluate(test_images,test_labels,verbose=2)

print(f"The Loss: {loss_score:.4f} and The Accuracy: {accuracy_score:.4f}")
# The Loss: 0.3336 and The Accuracy: 0.8832

