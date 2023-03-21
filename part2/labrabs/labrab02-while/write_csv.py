import csv


lst = [
    [1, 'Капуста'],
    [2, 'Морковь'],
    [3, 'Тыква'],
    [4, 'Брюква'],
]

column_names = ['id', 'title']  # определим заголовки столбцов
with open('vegetables.csv', 'w', encoding='utf8') as f:
    writer = csv.writer(f, delimiter=";", lineterminator='\n')  # зададим параметры
    writer.writerow(column_names)  # запишем в файл заголовки
    writer.writerows(lst) # запишем в файл все данные

"""
это пример сохранения списка данных в csv-файл
"""