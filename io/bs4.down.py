import bs4
import requests
import os
import urllib
folder = 'imgdown'
if not os.path.exists(folder):
    os.makedirs(folder)
os.chdir(folder)
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Cookie':''
}
url = 'https://www.bilibili.com/read/cv1865752/'
data = requests.get(url,headers)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
imgs = soup.select('div.article-holder > figure > img')
img_link = []
for i in imgs:
    img_link.append('https:'+i.get('data-src'))
for i in range(len(img_link)):
    urllib.request.urlretrieve(img_link[i], os.path.basename(img_link[i]))


