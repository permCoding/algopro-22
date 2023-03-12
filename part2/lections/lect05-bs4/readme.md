### bs4

```py
from bs4 import BeautifulSoup  # pip install bs4

soup = BeautifulSoup(src, "lxml")  # pip install lxml
soup = BeautifulSoup(src, "html.parser")  # уже есть
```

**1) .find() .find_all()**  

```py
page_h1 = soup.find("h1")

page_all_h1 = soup.find_all("h1")

user_name = soup.find("div", class_="user__name")
print(user_name.text.strip())

user_name = soup.find(class_="user__name").find("span").text
print(user_name)

user_name = soup.find("div", {"class": "user__name", "id": "aaa"}).find("span").text

find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")
for item in find_all_spans_in_user_info:
    print(item.text)

print(find_all_spans_in_user_info[0].text)

social_links = soup.find(class_="social__networks").find("ul").find_all("a")

for item in soup.find_all("a"):
    item_text = item.text
    item_url = item.get("href")
```

---  

**2) .find_parent() .find_parents()**  

```py
post_div = soup.find(class_="post__text").find_parent()

post_div = soup.find(class_="post__text").find_parent("div", "user__post")

post_divs = soup.find(class_="post__text").find_parents("div", "user__post")
```

**3) .next_element .previous_element**  

```py
next_el = soup.find(class_="post__title").next_element.next_element.text
next_el = soup.find(class_="post__title").find_next().text
```

**4) .find_next_sibling() .find_previous_sibling()**  

```py
next_sib = soup.find(class_="post__title").find_next_sibling()

prev_sib = soup.find(class_="post__date").find_previous_sibling()

post_title = soup.find(class_="post__date").find_previous_sibling().find_next().text
```

**5) .get() dict re**  

```py
links = soup.find(class_="some__links").find_all("a")

for link in links:
    link_href_attr = link.get("href")
    link_href_attr1 = link["href"]

    link_data_attr = link.get("data-attr")
    link_data_attr1 = link["data-attr"]

find_a_by_text = soup.find("a", text="Одежда")
find_a_by_text = soup.find("a", text="Одежда для взрослых")

import re
find_a_by_text = soup.find("a", text=re.compile("Одежда"))
find_all_clothes = soup.find_all(text=re.compile("([Оо]дежда)"))
```

---  
