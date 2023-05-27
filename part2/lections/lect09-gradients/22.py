# инвертируем цвет у пикселей по заданному правилу

from PIL import Image


def get_color_invert(color):
    """ инвертировать цвет пикселя """
    r, g, b = color
    return (255 - r, 255 - g, 255 - b)


name_file = 'белка.jpg'
path = './images/' + name_file
img = Image.open(path)
width, height = img.size

for y in range(height):
    for x in range(width):
        if y > x:  # определим такое правило - левый нижний
            color = img.getpixel((x, y))
            img.putpixel((x, y), get_color_invert(color))

img.save('./gradients/_' + 'белка.jpg')
img.show()
