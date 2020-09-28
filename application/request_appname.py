#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 3:15 PM
# @Author  : Charles He
# @File    : request_appname.py
# @Software: PyCharm


import requests
import re


class get_info():
    def __init__(self, voc):
        self.voc = voc
        self.result = []

    def get(self, voc, page):
        headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}
        url = 'https://appstore.huawei.com/search/{}/{}'.format(voc, page)
        html = requests.get(url, headers=headers)
        content = html.content.decode('utf-8')
        pattern = re.compile(r'title="(.*?)".*?href="/app/', re.S)
        resulti = re.findall(pattern, content)
        return resulti

    def main(self):
        for voc in self.voc:
            for i in range(1, 100):
                try:
                    resulti = self.get(voc, i)
                    if resulti == []:
                        break
                    else:
                        self.result.extend(resulti)
                except Exception as err:
                    print('no other pages,present page:{}'.format(i))
                    break
        self.result = list(set(self.result))
        for app in self.result:
            print(app)


# 1.newAppName:['news','新闻']
voc_news = ['游戏', '新闻', "直播", "唱歌"]
voc_notebook = ['game', '游戏']
voc_payments = ['payment', '付款']
get_info(voc_news).main()
