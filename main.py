#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2024/8/30 下午9:39 
# ide： PyCharm
# file: main.py
from flask import Flask, request
from xml.dom.minidom import parseString
import json
PATH_INDEX_SEND = './html/index.html'
PATH_INDEX_RECEIVED = './html/received/index.html'
INDEX_INSERT = 22

class QslListener:
    def __init__(self):
        self.qsl = Flask(__name__)

        @self.qsl.route('/qsl', methods=['POST'])
        def qsl():
            if request.method != 'POST':
                return "bad request"
            data_raw = json.loads(request.data)
            type_commit = data_raw['MsgType']
            time_commit = data_raw['Time']
            text_commit = data_raw['Text']
            if type_commit == 'Sent':
                return insert_index(text_commit,time_commit,path=PATH_INDEX_SEND)
            elif type_commit == 'Received':
                return insert_index(text_commit, time_commit,path=PATH_INDEX_RECEIVED)


def insert_index(text_insert, time_insert, path) -> str:
    text = '<tr><th>'+time_insert+'</th><th>'+text_insert+'</th></tr>\n'
    with open(path,'r') as f:
        lines = f.readlines()
        lines.insert(INDEX_INSERT, text)
    with open(path, "w") as f:
        f.writelines(lines)
        return 'Successful'


def main() -> None:
    aaa = QslListener()
    aaa.qsl.run(host='0.0.0.0', port=80)


if __name__ == "__main__":
    main()

