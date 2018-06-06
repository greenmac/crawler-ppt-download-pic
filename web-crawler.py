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
import requests
from bs4 import BeautifulSoup
import re

url="https://www.ptt.cc/bbs/ToS/index3852.html"
#要找出錯誤
reg_imgur_file=re.compile('http[s]?://i.imgur.com/\w+\.(?:jpg|png|gif)')

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
        images=reg_imgur_file(res.text)
        print(images)
