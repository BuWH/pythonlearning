# -*- coding: utf-8 -*-
import re
c = list(filter(None,re.split('^([a-zA-Z]+)(@)([a-zA-Z.]+)$','wenhe@gmail.com')))
print(c)