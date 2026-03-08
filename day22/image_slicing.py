import numpy as np
from PIL import Image

# load image
img = np.array(Image.open("grid_image_for_slicing.png"))

# crop the image
crop = img[80:200, 80:200]
#save the image
Image.fromarray(crop).save("cropped_image.png")
