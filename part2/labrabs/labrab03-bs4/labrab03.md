### LABRAB 03  

**bs4**  

---  

**task01**  

Дан адрес странички: https://pcoding.ru/parsing/01/page.html  
Собрать данные на отзывы: заголовок и текст отзыва.  
Сохранить полученные данные в формате json в файле feedbacks.json:  
```
[
	{
		"id": "тут порядковый номер",
		"title": "тут заголовок отзыва",
		"text": "тут текст отзыва"
	},
	...
]
```

---  

**task02**

Дана страница: https://pgatu.ru/today/  
Собрать данные по новостям: дата, название, ссылка, краткий текст.  
Сохранить в файле news.json.  
Данные собирать только с первой страницы - первые 10 новостей.  

---  

Смотреть методы библиотеки bs4, примеры и ссылки на документацию в папке лекции: **lect06-bs4**  

Примеры программ по библиотеке bs4 в папке: **lect06-bs4/00-bs4-examples**  

Если уже есть список объектов (словарей), то его можно сохранить в **json-файл** так:  

```py
import json

with open('results.json', 'w', encoding='utf8') as f:
    json.dump(teams, f, ensure_ascii=False, indent=4)
```

---  
