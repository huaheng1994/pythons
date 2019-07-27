import requests
import time
import os
from lxml import etree
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
}
def page(n):
    url =[]
    for i in range(1,n+1):
        k = 'http://jandan.net/ooxx/page-'+str(i)+'#comments'
        url.append(k)
    return url

def img_adress(url):
    html = requests.get(url, headers).content.decode('utf-8')
    tree1 = etree.HTML(html)
    img = tree1.xpath('//ol//p/a/@href')
    imgs =[]
    for i in img:
        imgs.append('http:'+i)
    return(imgs)


def download(url):
    res = requests.get(url,headers)
    with open(os.path.basename(url),'wb') as f: 
        f.write(res.content)

path = 'jiandan'
if os.path.exists(path) != True:
    os.makedirs(path)
os.chdir(path)
for i in page(1):
    for k in img_adress('http://jandan.net/ooxx/page-1#comments'):
        download(k)



