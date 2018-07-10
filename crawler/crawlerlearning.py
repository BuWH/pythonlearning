# coding: utf-8
import requests
payload = {'wd' : 'haha'}
r = requests.get('http://bbs.byr.cn');
print(r.text.encode('utf-8'))