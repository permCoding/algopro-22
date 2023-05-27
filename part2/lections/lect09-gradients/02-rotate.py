# повернуть рисунок

from PIL import Image


def a():
    img = Image.open("./images/color.jpg")
    img = img.rotate(45)
    img.show()


def b():
    with Image.open("./images/color.jpg") as img:
        img.rotate(180).show()


def c():
    with Image.open("./images/color.jpg") as img:
        new_img = img.rotate(222)
    img.show()
    new_img.show()


b()
