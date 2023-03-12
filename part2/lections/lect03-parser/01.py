import requests


url = "https://pcoding.ru/darkNet.php"
obr = requests.get(url)  # <Response [200]>
obr.encoding = "utf8"
html = obr.text

print(html)
