#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 11:24 AM
# @Author  : Charles He
# @File    : batch_web_request.py
# @Software: PyCharm

import requests
import csv
import re
import random
import time
import socket
import http.client
from bs4 import BeautifulSoup
import pandas as pd


# 以抓取百度全境封锁2吧内容为例子
# 基本操作可以看回single_web_request
# 两种方法：构造url 和 匹配"下一页"


# 基本网页申请
def get_content(url, data=None):
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Encoding": "gzip",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }

    timeout = random.choice(range(80, 180))
    while True:
        try:
            rep = requests.get(url, headers=header, timeout=timeout)
            rep.encoding = "utf-8"
            break

        except socket.timeout as e:
            print('3:', e)
            time.sleep(random.choice(range(8, 15)))

        except socket.error as e:
            print('4:', e)
            time.sleep(random.choice(range(20, 60)))

        except http.client.BadStatusLine as e:
            print('5:', e)
            time.sleep(random.choice(range(30, 80)))

        except http.client.IncompleteRead as e:
            print('6:', e)
            time.sleep(random.choice(range(5, 15)))

    return rep.text

def get_shape(html_text):
    final = []
    reg = re.compile('<[^>]*>')
    bs = BeautifulSoup(html_text, "html.parser")
    body = bs.body

    data = body.find("div", {"class": "main_"})
    ul = data.find("table", {"class": "table"})
    trs = ul.find_all("tr")
    for i in trs:
        data_1 = i.find("td")
        if data_1:
            test_string = re.sub(reg, "", str(data_1))
            if test_string != '':
                final.append(test_string)

    return final

# 检测最后一页
def get_finalpage(html_text):
    pattern = re.compile('<li class=\"disabled\">') # 此部分因网页而异

    bs = BeautifulSoup(html_text, "html.parser")
    body = bs.body
    data = body.find_all("ul", {"class": "pagination"})
    page = re.findall(pattern, str(data[1]))
    print(page)
    return page


if __name__ == '__main__':
    final_result = []
    alpht = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']

    # for v in alpht:

    for i in range(1, 50):
        url = "http://www.resgain.net/english_names_a_{}.html".format(i) # 构造网页
        html = get_content(url)
        result = get_shape(html)
        if len(result) != 0:
            for j in result:
                final_result.append(j)
        else:
            break

    print(len(final_result))