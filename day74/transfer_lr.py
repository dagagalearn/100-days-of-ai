import tensorflow as tf
from tensorflow.keras import layers,models


base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224,224,3),
    include_top=False,
    weights="imagenet"
)

base_model.trainable=False
model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dropout(0.2),
    layers.Dense(2,activation="softmax")
])

model.compile(optimizer = "adam", loss="categorical_crossentropy",metrics=["accuracy"])

model.summary()




