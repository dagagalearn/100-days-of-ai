import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers

data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal_and_vertical"),
    layers.RandomRotation(0.2),
    layers.RandomZoom(0.1),
    layers.RandomContrast(0.2),
])

def visualize_aug(img_path):
    img = tf.keras.utils.load_img(img_path, target_size=(180, 180))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    plt.figure(figsize=(10, 10))
    for i in range(9):
        augm_img = data_augmentation(img_array)
        axis = plt.subplot(3, 3, i + 1)
        plt.imshow(augm_img[0].numpy().astype("uint8"))
        plt.axis("off")
        plt.title(f"variation {i + 1}")
        
    plt.tight_layout()
    plt.show()

visualize_aug("image.jpg")
