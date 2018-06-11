#16回之前寫的
# import requests
# requests.get("https://www.ptt.cc/bbs/NBA/index.html")
# res=requests.get("https://www.ptt.cc/bbs/NBA/index.html")
# x=res.text
# # print(x)

# from bs4 import BeautifulSoup
# soup=BeautifulSoup(res.text,"html.parser")
# tag_name="div.title a"
# articles=soup.select(tag_name)
# print(articles)

# for art in articles:
#     print(art)

# for atr in articles:
#     print(art['href'],art.text)

#17回之後
"""
#還未設定指定資料夾跟設計成function的時候
import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlretrieve
import os

url="https://www.ptt.cc/bbs/ToS/index3852.html"
reg_imgur_file=re.compile('http[s]?://[i.]*imgur.com/\w+\.(?:jpg|png|gif)')
for round in range(3):
    res=requests.get(url)
    soup=BeautifulSoup(res.text,"html.parser")
    articles=soup.select("div.title a")
    pagin=soup.select('div.btn-group-paging a')
    # page2_url=pagin[1]['href']
    next_url="https://www.ptt.cc"+pagin[1]['href']
    url=next_url


    for article in articles:
        print(article.text,article['href'])
        res=requests.get("https://www.ptt.cc"+article['href'])
        images=reg_imgur_file.findall(res.text)
        print(images)
        for image in set(images):
            ID=re.search('http[s]?://[i.]*imgur.com/(\w+\.(?:jpg|png|gif))',image).group(1)
            print(ID)
            urlretrieve(image,ID)

"""

#設定指定資料夾,還有改成function
import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlretrieve
import os
import sys

def download_images(articles):
    for article in articles:
        print(article.text,article['href'])
        if not os.path.isdir(os.path.join('download',article.text)):
            os.mkdir(os.path.join('download',article.text))
        res=requests.get("https://www.ptt.cc"+article['href'])
        images=reg_imgur_file.findall(res.text)
        print(images)
        for image in set(images):
            ID=re.search('http[s]?://[i.]*imgur.com/(\w+\.(?:jpg|png|gif))',image).group(1)
            print(ID)
            urlretrieve(image,os.path.join('download',article.text,ID))

def crawler(pages=3):
    if not os.path.isdir('download'):
        os.mkdir('download')
    url="https://www.ptt.cc/bbs/ToS/index3852.html"
    reg_imgur_file=re.compile('http[s]?://[i.]*imgur.com/\w+\.(?:jpg|png|gif)')
    for round in range(pages):
        res=requests.get(url)
        soup=BeautifulSoup(res.text,"html.parser")
        articles=soup.select("div.title a")
        pagin=soup.select('div.btn-group-paging a')
        # page2_url=pagin[1]['href']
        next_url="https://www.ptt.cc"+pagin[1]['href']
        url=next_url

        download_images(articles)

reg_imgur_file=re.compile('http[s]?://[i.]*imgur.com/\w+\.(?:jpg|png|gif)')
# print(sys.argv)
# print(int(sys.argv[1]))
crawler(int(sys.argv[1]))
