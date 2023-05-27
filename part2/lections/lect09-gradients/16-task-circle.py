# понизим яркость у заданного количества пикселей

from itertools import count
from PIL import Image
from random import randint

img = Image.open("./images/белка.jpg")

width, height = img.size

count, i = 9000, 0
while i < count:
    i += 1
    cur_x = randint(0, width-1)
    cur_y = randint(0, height-1)
    r, g, b = img.getpixel((cur_x, cur_y))
    r //= randint(1, 5); 
    g //= randint(1, 5); 
    b //= randint(1, 5); 
    color = (r, g, b)
    img.putpixel((cur_x, cur_y), color)

img.show()

"""
при таком подходе некоторые пиксели
будут повторяться
то есть в реальности будут изменены не 9000
пикселей, а, например, 8822

задача 1
- придумайте как генерировать точки без повтора
- если задано 2000, то должно быть 2000 точек изменено

задача 2
- придумайте как генерировать красные точки 
  только за пределами окружности, вписанной в рамку картинки
- смотрите пример результата такой генерации:
  './gradients/_circle.jpg'
  
"""