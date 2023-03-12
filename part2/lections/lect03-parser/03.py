import requests


ua = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"    
}
url = "https://pcoding.ru/darkNet.php"
obr = requests.get(url, headers=ua)  # <Response [200]>
obr.encoding = "utf8"
html = obr.text

f = open("pcoding.html", 'w', encoding='utf8')
f.write(html)
