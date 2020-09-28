#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 3:09 PM
# @Author  : Charles He
# @File    : 粤拼转换接口.py
# @Software: PyCharm

import requests
import json
import re
from bs4 import BeautifulSoup


class Yueping_translate():
    def __init__(self, trans_word):
        # 设定url // data为传入的数据 // headers中的cookie必须填写，不然会bad request
        self.url = "https://www.chineseconverter.com/cantonesetools/zh-tw/cantonese-to-jyutping"
        self.data = {
            "_csrf-frontend": "l_5bFXWpnZmMgCS0FfBx1mh7JP3joYI_q4fjvHCiWgH9zQtXNs3-8cS5HPwsgEPlBwMVmoTVxA7N_7bxM-gKUA==",
            'CantoneseToJyutping[input]': trans_word}
        self.headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "refer": "https://www.chineseconverter.com/cantonesetools/zh-tw/cantonese-to-jyutping",
            'cookie': '__cfduid=d0678cffbdd806a8c33e494e2ab1ddef91585534168; chinese-converter-frontend=7nqhh1odrpojiuoah5vas7lh01; _csrf-frontend=788ef628915acf7d55670ff35aa518222f29154ed7542c985edaf25ff45f51b0a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22j3PBCdchH98H9p23ox1ggtF1fxUMCJPQ%22%3B%7D; __utmc=54387834; __utmz=54387834.1585534171.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __gads=ID=2bd46f9a8a9b4ab2:T=1585534170:S=ALNI_MYiUXVh2qRwC62njyXbJQg22IUd2w; __utma=54387834.38120099.1585534170.1585534170.1585637706.2; _pk_id.1.2a42=aeb28e52866b3219.1585534992.2.1585637944.1585637705.'}

    def run(self):
        # 创建请求， 发送请求， 爬取信息
        res = requests.post(self.url, data=self.data, headers=self.headers)
        # 解析结果
        str_json = res.content.decode("utf-8")
        bs = BeautifulSoup(str_json, "html.parser")
        body = bs.body
        # location of the result
        result = body.find("div", {"class": "thumbnail result-html"}).string.lstrip().rstrip()
        print(result)
        return result


if __name__ == "__main__":
    a = Yueping_translate("有识之士")
    a.run()
