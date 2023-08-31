#!/usr/bin/env python3
from PIL import Image

my_image = Image.open('confetti-lying-near-present.jpg')

print("current size is: {}".format(my_image.size))

# Define the target size as a tuple
target_size = (1920, 1080)

# Resize the image using a specified resampling filter
resized_image = my_image.resize(target_size, Image.LANCZOS)

resized_image.save('new-image-1920.jpeg')

print("current new-image size is: {}".format(resized_image.size))

