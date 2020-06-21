import requests
from bs4 import BeautifulSoup
import csv
URL = 'https://onlinetestpad.com/ru/tests/psychological/psychodiagnostics'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
HOST = 'https://onlinetestpad.com'
FILE = 'tests.csv'
def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='card card-item-box')

    tests = []
    for item in items:
        tests.append({
            'title': item.find('h3').get_text(strip=True),
            'link': HOST + item.find('a').get('href'),
            'image': item.find('img', class_='overlay-figure overlay-spin').get('src'),
            'desc': item.find('p', class_='card-text').get_text(strip=True)
        })
    return tests

def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(['Название теста', "Ссылка", "Картинка", "Описание"])
        for item in items:
            writer.writerow(item['title'], item['link'], item['image'], item['desc'],)



def parse():
    html = get_html(URL)
    if html.status_code == 200:
        tests = get_content(html.text)
        save_file(tests, FILE)
    else:
        print('error')


parse()