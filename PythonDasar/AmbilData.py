import requests
from bs4 import BeautifulSoup

# membuat request ke website
url = 'https://www.example.com'
response = requests.get(url)

# parsing html menggunakan BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# mencari elemen html yang diinginkan
title = soup.title.text
paragraphs = [p.text for p in soup.find_all('p')]

# menampilkan hasil
print('Title:', title)
print('Paragraphs:', paragraphs)
