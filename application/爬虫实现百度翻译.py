import requests
import json
import sys


class Baidu_fanyi():
    # 可根据个人需要添加headers // 或修改为英译中等多个版本的检测
    def __init__(self, url, trans_word):
        self.url = url
        self.data = {'kw': trans_word}

    def run(self):
        res = requests.post(url=self.url, data=self.data)
        str_json = res.content.decode("utf-8")
        myjson = json.loads(str_json)
        print(myjson['data'][0]['v'])


if __name__ == "__main__":
    a = Baidu_fanyi(url="https://fanyi.baidu.com/sug", trans_word="python")
    a.run()
