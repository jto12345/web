#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/14 0014 下午 3:09
# @Author  : jiangtao
# @Site    : 
# @File    : jiangtao.py
# @Software: PyCharm
# #
import urllib3
from urllib.request import urlopen

html = urlopen("http://www.baidu.com")

print(html.read())


# import urllib3
#
# dir(urllib3)
#
# print(dir())