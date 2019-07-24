import csv
import requests
from bs4 import BeautifulSoup
url = 'http://www.100ppi.com/monitor/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
}
res = requests.get(url, headers)
soup = BeautifulSoup(res.text, 'html.parser')
div1 = soup.find_all("div", attrs={"class":"right fl"})
tab1 = div1[0].find_all("table")
trs = tab1[0].find_all("tr")
table_names = {}
table_name = ""
idx = 0
for i in trs:
    idx += 1
    if idx == 1:
        continue
    tds = i.find_all("td")
    if len(tds) == 5:
        table_names[table_name].append([tds[0].find("a").text, tds[1].text, tds[2].text, tds[3].text, tds[4].text])
    if len(tds) == 1:
        b = tds[0].find("b")
        table_names[b.text] = []
        table_name = b.text
with open("商品价格.csv",'w', newline = '') as f: 
    writer = csv.writer(f) 
    for k in table_names:
        writer.writerow(k)
        lst = table_names[k]
        for i in lst:
            writer.writerow(i)


