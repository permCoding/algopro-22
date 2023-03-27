from bs4 import BeautifulSoup
import json
from time import sleep
from parsing import get_html


def get_books(html):
    soup = BeautifulSoup(html, 'html.parser')
    prods = soup.find_all('article')
    books = []
    pref = "https://www.chitai-gorod.ru"
    for prod in prods:
        head = prod.find('div', class_="product-title__head").text.strip()
        author = prod.find('div', class_="product-title__author").text.strip()
        price = prod.find('div', class_="product-price__value").text.strip().replace('\xa0','')
        ref = pref + prod.find('a', class_="product-card__row")['href']
        books.append([head,author,price,ref])
    return books

   
def get_all_books(count=0):
    all_books = []
    page = 0
    sleep(1)
    while True:
        page += 1
        if count!=0 and page>count: break
        print(page)
        url = f"https://www.chitai-gorod.ru/catalog/books/nauchnaya-fantastika-9693?page={page}"
        try:
            html = get_html(url)
            lst = get_books(html)
            all_books.extend(lst)
        except:
            pass
    return all_books

    
def write_json(filename, lst):
    def get_dict(i, e):
        name_columns = ['id', 'head', 'author', 'price', 'ref']
        values = [i+1] + e
        return dict(zip(name_columns, values))    

    lst_w = [get_dict(i,e) for i,e in enumerate(lst)]
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(lst_w, f, indent=4, ensure_ascii=False)


all_books = get_all_books(3)
write_json('all_books_3.json', all_books)

"""

"""