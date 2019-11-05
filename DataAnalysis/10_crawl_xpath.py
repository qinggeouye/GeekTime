import os

import requests
from lxml import etree
from selenium import webdriver

search_text = '王祖贤'
start = 0  # 请求 url 的 start 从 0 开始，每一页间隔 15，有 6 页
total = 90
limit = 15

# 电影海报图片地址
src_xpath = "//div[@class='item-root']/a[@class='cover-link']/img[@class='cover']/@src"
# 电影海报图片title
title_xpath = "//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']"

# 保存目录
pic_path = '10/xpath'  # 相对目录
# WebDriver 创建一个 Chrome 浏览器的 drive
driver = webdriver.Chrome('./chromedriver')  # MAC 版本


# 创建图片保存路径
def mk_save_path(pic_path_):
    if not os.path.exists(pic_path_):
        os.makedirs(pic_path_)
    return os.getcwd() + '/' + pic_path_ + '/'


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


def get_response_xpath():
    save_path = mk_save_path(pic_path)
    for i in range(start, total, limit):
        requests_url = 'https://search.douban.com/movie/subject_search?search_text=' + search_text + '&cat=1002' + \
                       '&start=' + str(i)
        driver.get(url=requests_url)
        html = etree.HTML(driver.page_source)
        src_list = html.xpath(src_xpath)
        title_list = html.xpath(title_xpath)
        for src, title in zip(src_list, title_list):
            download(src, title.text, save_path)


if __name__ == '__main__':
    get_response_xpath()
