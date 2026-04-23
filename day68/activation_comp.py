import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.datasets.fashion_mnist import load_data
import matplotlib.pyplot as plt
from tensorflow import keras

(train_img, train_label),(test_img,test_label) = load_data()
train_img = train_img/255
test_img = test_img/255

plt.imshow(train_img[10],cmap="gray")
plt.colorbar()
plt.show()

model_1 = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128,activation="relu"),
    keras.layers.Dense(128,activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

model_2 = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128,activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

model_3 = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(4,activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

model_4 = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128,activation="sigmoid"),
    keras.layers.Dense(10, activation="softmax")
])

model_5 = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(64,activation="relu"),
    keras.layers.Dense(16,activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

#compiling
model_1.compile(optimizer="adam",loss="sparse_categorical_crossentropy", metrics=['accuracy'])
model_2.compile(optimizer="adam",loss="sparse_categorical_crossentropy", metrics=['accuracy'])
model_3.compile(optimizer="adam",loss="sparse_categorical_crossentropy", metrics=['accuracy'])
model_4.compile(optimizer="adam",loss="sparse_categorical_crossentropy", metrics=['accuracy'])
model_5.compile(optimizer="adam",loss="sparse_categorical_crossentropy", metrics=['accuracy'])

history_1 = model_1.fit(train_img, train_label,validation_data=(test_img,test_label),epochs=50)
history_2 = model_2.fit(train_img, train_label,validation_data=(test_img,test_label),epochs=50)
history_3 = model_3.fit(train_img, train_label,validation_data=(test_img,test_label),epochs=50)
history_4 = model_4.fit(train_img, train_label,validation_data=(test_img,test_label),epochs=50)
history_5 = model_5.fit(train_img, train_label,validation_data=(test_img,test_label),epochs=50)

histories = [history_1, history_2,history_3,history_4,history_5]
for i, h in enumerate(histories):
  plt.plot(h.history["val_accuracy"],label=f"Model {i+1}", linewidth=3)
plt.xlabel("epoch")
plt.ylabel("Accuracy")
plt.title("Model Comparison")
plt.legend()
plt.grid(True)
plt.show()

plt.plot(history_1.history["loss"],label="Loss")
plt.plot(history_1.history["val_loss"],label="Validation Loss")
plt.grid(True)
plt.xlabel("epochs")
plt.ylabel("Loss/Val_loss")
plt.legend()
plt.show()

