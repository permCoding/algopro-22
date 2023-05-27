# инверсия rgb-рисунка

from PIL import Image

img = Image.open("./images/ждун.jpeg")  # rgb-цвета
width, height = img.size

for y in range(height):
    for x in range(width):
        r, g, b = img.getpixel((x,y))
        # r = 255 - r
        # g = 255 - g
        b = 255 - b  # тут только синий инверсный
        img.putpixel((x, y), (r,g,b))

img.show()

"""
был чёрный
R   G   B
0   0   0 
стал синий:
0   0  255

был белый
 R   G   B
255 255 255 
стал желтый:
255 255  0

"""
