# инверсия серого рисунка

from PIL import Image

img = Image.open("./images/dog.jpg")  # оттенки серого
width, height = img.size

for y in range(height):
    for x in range(width):
        grey = img.getpixel((x, y))
        grey = 255 - grey  # инвертируем цвет
        img.putpixel((x, y), grey)

img.show()
