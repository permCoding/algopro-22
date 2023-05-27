# понизим градиентно яркость у всех пикселей

from PIL import Image

img = Image.open("./images/белка.jpg")
width, height = img.size
ky = 256 / height  # чтобы 256 уровней уложились в высоту

for y in range(height):
    for x in range(width):
        r, g, b = img.getpixel((x, y))
        r -= int(y * ky//1.5)
        g -= int(y * ky//1.2)
        b -= int(y * ky)
        img.putpixel((x, y), (r, g, b))

img.show()
