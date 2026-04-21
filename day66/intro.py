import tensorflow as tf
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.fashion_mnist.load_data()

print(f"The train shape: {train_images.shape}")
print(f"The test shape: {test_images.shape}")

plt.figure()
plt.imshow(train_images[0], cmap='gray')
plt.colorbar()
plt.title(f"Label: {train_labels[0]}")
plt.show()
