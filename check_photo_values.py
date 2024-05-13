from numpy import asarray
from PIL import Image

img = Image.open("hp_16.jpg")

print(f"image size is {img.size}")
print(f"image mode is {img.mode}")
print(f"image value is {asarray(img)}")
