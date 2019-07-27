import requests
import bs4
#from bs4 import BeautifulSoup
url = 'https://www.bilibili.com/read/cv3104709?from=rank_1'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
}
res = requests.get(url, headers)
soup = bs4.BeautifulSoup(res.text, 'lxml')
# with open('2.html', 'w', encoding='utf-8') as f:
#     f.write(res.text)
#divs = soup.select('div.page-container > figure')
#divs = soup('div', class_="article-holder")
#divs = soup('div', class_="article-holder")
divs = soup('img',class_="fanju-card")
#print(divs)
for i in divs:
    print(i.get('data-src'))