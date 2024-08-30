#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2024/8/30 下午10:44 
# ide： PyCharm
# file: main.py.py
import requests
import datetime
URL = r'http://127.0.0.1/qsl'


def main():
    type_commit = '"Sent"'
    temp_input = int(input('请选择记录类型，收卡:0, 寄卡:1\n'))
    if not (temp_input == 0 or temp_input == 1):
        temp_input = int(input('请重新选择记录类型，收卡:0, 寄卡:1\n'))
    if temp_input == 1:
        type_commit = '"Sent"'
    elif temp_input == 0:
        type_commit = '"Received"'
    else:
        print('无效输入,程序退出!')
        return -1

    text_input = str(input('请输入记录呼号,中间不要空格,使用半角逗号隔开,使用回车结束输入: '))
    text_commit = text_input
    time_commit = datetime.datetime.now().strftime("%Y-%m-%d")

    text_commit = '"' + text_commit + '"'
    time_commit = '"' + time_commit + '"'

    if temp_input == 1:
        print('以下内容将上传至卡片发送记录，请输入1确认上传\n')
        print(time_commit + '\t' + text_commit)
        if input() == '1':
            print(send(type_commit, text_commit, time_commit, url=URL))

        else:
            return
    else:
        print('以下内容将上传至卡片接收记录，请输入1确认上传\n')
        print(time_commit + '\t' + text_commit)
        if input() == '1':
            print(send(type_commit, text_commit, time_commit, url=URL))

        else:
            return


def send(type_commit,text_commit, time_commit, url) -> str:
    raw = '{"MsgType":' + type_commit + ','\
        '"Time":' + time_commit + ','\
        '"Text":' + text_commit + '}'
    x = requests.post(url, data=raw)
    return '成功!'


if __name__ == "__main__":
    main()



