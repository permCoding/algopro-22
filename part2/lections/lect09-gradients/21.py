# понизим неравномерно яркость у всех пикселей

from PIL import Image

img = Image.open("./images/белка.jpg")
width, height = img.size
ky = 256 / height

for y in range(height):
    for x in range(width):
        r, g, b = img.getpixel((x, y))
        r -= int(y * ky)
        g -= int(y/9 * ky)
        b += int(y/6 * ky)
        b = min(255, b)
        img.putpixel((x, y), (r, g, b))

img.show()
