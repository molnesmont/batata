import requests
import json
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
url = 'https://psychojournal.ru/article/'
host = 'https://psychojournal.ru'

def get_html(url, page=''):
    url = url + str(page)
    r = requests.get(url, headers=headers)
    # print(r.url)
    # print(url+str(params))
    return r

def pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    page = soup.find('span', class_='page').find_all('a')
    if page:
        return int(page[-1].get_text())
    else:
        return 1
    # print(page)


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='row-fluid mr side')

    artcl = []
    for item in items:
        artcl.append({
            'title': item.find('h4').get_text(strip=True),
            'link': item.find('a').get('href'),
            'text': item.find('p').get_text(strip=True),
            'img': host + item.find('img').get('src')

        })
    return artcl


def parse():
    html = get_html(url)
    if html.status_code == 200:
        article = []
        pages = pages_count(html.text)
        for page in range(1, pages+1):
            html = get_html(url, page='page/' + str(page))
            print(f'Страница {page} из {pages}')
            article.extend(get_content(html.text))
        with open('article.json', 'w', encoding="utf-8") as f:
            json.dump(article, f, ensure_ascii=False, indent=2 )
    else:
        print("Error")


parse()