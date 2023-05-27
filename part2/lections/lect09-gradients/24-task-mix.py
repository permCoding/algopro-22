# и зальём ею какой-нибудь рисунок

from PIL import Image

img = Image.open("./images/белка.jpg")
width, height = img.size
ky = 256 / height
kx = 256 / width

for y in range(height):
    for x in range(width):
        r, g, b = img.getpixel((x, y))
        # просто смешиваем цвет градиента с цветом рисунка
        r = (r+int(y * ky))//2
        g = (g+int(x * kx))//2
        b = (b+int(255 - (y*ky)))//2
        img.putpixel((x, y), (r, g, b))

img.save('./gradients/_' + 'example.jpg')
img.show()
