import requests
import bs4
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
def img_adress(url):
    #url = 'https://bcy.net/coser/toppost100?type=week&date=20190725'
    res = requests.get(url,headers)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    # with open('2.html', 'w', encoding='utf-8') as f:
    #     f.write(res.text)
    adrs = soup.select('#content-box > div > ul.l-clearfix.gridList.smallCards.js-workTopList > li > a')
    adress_link = []
    for i in adrs:
        adress_link.append('https://bcy.net'+i.get('href'))
    return(adress_link)

#def img_down(url):
url = 'https://bcy.net/item/detail/6715659515250868488'
res = requests.get(url,headers)
soup = bs4.BeautifulSoup(res.text, 'lxml')
imgs = soup.select('#app > div > div.container > div > div.col-big > div._box.mb10 > article > div.content > div.album > div:nth-child(2) > div > div > img')
print(imgs)
