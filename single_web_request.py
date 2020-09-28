#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 11:24 AM
# @Author  : Charles He
# @File    : batch_web_request.py
# @Software: PyCharm


#coding: UTF-8

import requests
import csv
import random
import time
import socket
import http.client
from bs4 import BeautifulSoup
import pandas as pd


# 基本网页申请 苏州天气网7天天气

def get_content(url, data=None):
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/80.0.3987.132 Safari/537.36 "
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


# 内容抓取
def get_data(html_text):
    final = []
    bs = BeautifulSoup(html_text, "html.parser")
    body = bs.body
    data = body.find("div", {"id": "7d"})
    ul = data.find("ul")
    li = ul.find_all("li")
    for day in li:
        temp = []
        date = day.find("h1").string
        temp.append(date)
        inf = day.find_all("p")
        temp.append(inf[0].string)

        if inf[1].find("span") is None:
            tem_high = None
        else:
            tem_high = inf[1].find("span").string.replace('℃', '')

        tem_low = inf[1].find("i").string.replace('℃', '')
        temp.append(tem_high)
        temp.append(tem_low)
        final.append(temp)

    final_df = pd.DataFrame(final, columns=["date", "weather", "highest_temperture", "lowest_temperture"])

    return final_df


if __name__ == '__main__':
    url = 'http://www.weather.com.cn/weather/101190401.shtml'
    html = get_content(url)
    result = get_data(html)
    print("-----------------------------")
    print(result)
    print("-----------------------------")



