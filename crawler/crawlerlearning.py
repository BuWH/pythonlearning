# coding: utf-8
import requests,time
from bs4 import BeautifulSoup
page = 1
target = 'http://www.qiushibaike.com/hot/page/' + str(page)
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15'}
try:
    r = requests.get(url=target, headers=headers,verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    print(r.text)
except requests.Timeout as e:
    print(e)

def hahaha(tag):
    return tag.name == 'div' and tag.attrs == {'class':'article block untagged mb15 typs_hot'}

def download_pic(src,id):
    with open('%d.jpg' % id,'wb') as f:
        f.write(requests.get(src).content)

for content in soup.find_all(hahaha):
    print(content.string)