import numpy as np

# Convulation is a technique used mainly in image detection
# Why use convulations:
"""
Assume I have 1920x1080 image. Think about training this image in NN, it would take eternity to get something out of it.
So, how do we recognize images? The short answer is Convulations(*). 

"""
# Intuitive explanation: Identifying human image
"""
Let's say we wish to make a program that takes an image and tells if it is human or not(which we can do in seconds but it is difficult for computers).
We take the iamge as a grid of gray scale (0-black , 1-white). We make a new array of numbers called a filter.
We convulute the image with the filter. The filter as its name suggests it filters the image to what we need. 
filter_1 might filter an eyes, filter_2 might identify a mouth...
the we filter the head from our previous filters (eye,hair,nose,mouse...) and we do same for hands , legs, posture etc.

What we get after convulations is called feature map. Then we don't need all the output we just need a part that detects the part of the image.
so, there is a technique called pooling. It reduces the computation time, reduces overfitting,it gives only what we need. It might have different types:
max pooling or average pooling. When pooling there is something called striding it determines how we pool the image(by jumping 1 grid or 2 grid ,n grid). 

"""
# Convulation example

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(np.convolve(arr1,arr2))

"""
4 = 1*4 (numbers adding up to 5)
13 = 1*5 + 2*4 (numbers adding up to 6)
28 = 1*6+2*5+3*4 (numbers adding up to 7)
27 = 2*6+3*5 (numbers adding up to 8)
18 = 3*6 (numbers adding up to 9)
             

"""
# Vertical Edge Detector Example
# 1 represents white, 0 represents black
image_chunk = np.array([
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 1, 0, 0]
])

# This filter looks for transitions from 1 to 0 (edges)
vertical_filter = np.array([
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]
])

print("This looks for vertical edge irrespective of where the vertical edge is positioned")
print("==================================================")
