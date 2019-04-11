#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 1:46 PM
# @Author  : pentakill
# @File    : dicPratice.py
# @Software: PyCharm

import requests

datas = {"name":"python","age":25}
print("年龄：",datas["age"])

url = "http://www.baidu.com"
response = requests.get(url)
print(response.status_code)