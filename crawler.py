# -*- coding: utf-8 -*-  

#输出时使用 utf-8 格式
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#函数主体如下

import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://cdshishi.net')
    f = open('website.json','w+b')
    f.write(response.read())
    #print(response.info())
except urllib.error.URLError as e:
    if hasattr(e,'reason'):
        print('URLerror reason:'+str(e.reason))
    if hasattr(e,'code'):
        print('URLerror code:'+str(e.code))
except urllib.error.HTTPError as e:
    if hasattr(e,'reason'):
        print('HTTPerror reason:'+str(e.reason))
    if hasattr(e,'code'):
        print('HTTPerror code:'+str(e.code))
else:
    print('Crawler is running well.')