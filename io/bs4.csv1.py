import csv
import requests
from bs4 import BeautifulSoup
url = 'http://www.100ppi.com/mprice/list-11-'
table_name = []
def url_open(furl):
    #url = 'http://www.100ppi.com/mprice/list-11-1.html'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    }
    res = requests.get(furl, headers)

    soup = BeautifulSoup(res.text, "lxml")
    table = soup('table', class_="lp-table mb15")
    trs = table[0]('tr')
    # ths = trs[0].find_all("th")
    # print(ths[0].text)
    table_names = []
    idx = 0
    for i in trs:
        idx += 1
        if idx == 1:
            continue
            # ths = i.find_all("th")
            # table_names.append([ths[0].text, ths[1].text, ths[2].text, ths[3].text, ths[4].text])
        if idx != 1:
            tds = i.find_all("td")
            table_names.append([tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text])
    return table_name.append(table_names)
# print(table_names)
#for i in trs:
# with open('1.html', 'w', encoding='utf-8') as f:
#     f.write(res.text)
page = 10
for i in range(1,page+1):
    furl = url + str(i)+'.html'
    url_open(furl)

with open("价格.csv",'w', newline = '') as f: 
    writer = csv.writer(f) 
    for i in range(page):
        pp = table_name[i]
        for k in pp:
            writer.writerow(k)
