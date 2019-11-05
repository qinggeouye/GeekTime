# coding: utf-8
import os

import requests
import json


# 下载图片
def download(src, pic_id, save_path_):
    directory = save_path_ + str(pic_id) + '.jpg'
    try:
        pic = requests.get(src, timeout=10)
        fp = open(directory, 'wb')
        fp.write(pic.content)
        fp.close()
    except requests.exceptions.ConnectionError:
        print('图片如无法下载')


# 获取返回页面内容
def get_resp(query_, limit_, start_):
    url_ = 'https://www.douban.com/j/search_photo?q=' + query_ + '&limit=' + str(limit_) + '&start=' + str(start_)
    html_ = requests.get(url_).text  # 得到返回结果
    response_ = json.loads(html_, encoding='utf-8')  # 将 JSON 格式转换为 Python 对象
    return response_


def mk_save_path(pic_path_):
    if not os.path.exists(pic_path_):
        # os.mkdir(pic_path)
        os.makedirs(pic_path_)
    return os.getcwd() + '/' + pic_path_ + '/'


# 循环 请求全部的 url
def get_response_json():
    save_path = mk_save_path(pic_path)
    for i in range(start, total, limit):
        response = get_resp(query, limit, i)
        for image in response['images']:
            print(image['src'])  # 查看当前下载的图片地址
            download(image['src'], image['id'], save_path)  # 下载一张图片


query = '王祖贤'
limit = 20  # 请求 url 的 start 从 0 开始，每次请求间隔 20
start = 0
# 获取图片总数
total = get_resp(query, limit, start)['total']
# 保存目录
pic_path = '10/json'  # 相对目录

if __name__ == "__main__":
    get_response_json()
