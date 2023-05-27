# понизим случайным образом яркость 
# пикселей с определённым шагом

from PIL import Image
from random import randint

img = Image.open("./images/белка.jpg")

width, height = img.size

for y in range(0, height, 2):  # шаг 2
    for x in range(0, width, 3):  # шаг 3
        r, g, b = img.getpixel((x, y))
        r //= randint(1, 5)
        g //= randint(1, 5)
        b //= randint(1, 5)
        color = (r, g, b)
        img.putpixel((x, y), color)

img.show()
