import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlretrieve
import os


def download_images(articles):
    for article in articles:
        # print(article.text,article['href'])
        article_text = article.text
        if not os.path.isdir(os.path.join('download', article_text)):
            os.mkdir(os.path.join('download', article_text))
        res = requests.get('https://www.ptt.cc'+article['href'])
        images = reg_imgur_file.findall(res.text)
        # print(images)

        for image in set(images):
            ID = re.search('http[s]?://[i.]*imgur.com/(\w+\.(?:jpg|png|gif))',image).group(1)
            # print(ID)
            # urlretrieve(image, os.path.join('download', article_text, ID)) # 再細分一個資料夾會出錯,不知為何
            urlretrieve(image, os.path.join('download', ID))

def crawler(pages=3):
    if not os.path.isdir('download'):
        os.mkdir('download')
    url = 'https://www.ptt.cc/bbs/Beauty/index.html'
    for round in range(pages):
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser') # text指的是內文結果
        title = 'div.title a'
        articles = soup.select(title)
        paging = soup.select('div.btn-group-paging a')
        next_url = 'https://www.ptt.cc'+paging[1]['href']
        url = next_url
        download_images(articles)

reg_imgur_file=re.compile('http[s]?://[i.]*imgur.com/\w+\.(?:jpg|png|gif)')
crawler()