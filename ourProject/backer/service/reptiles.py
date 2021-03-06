from django.utils.datetime_safe import datetime
from bs4 import BeautifulSoup

import requests
import re
import os

from ..models import Image

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/76.0.3809.132 Safari/537.36'}
count = 1


def get_url(url_value, word):
    img_url = ""
    # 百度图片的链接
    if url_value == 1:
        img_url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=img_word&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=img_word&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=img_page&rn=30&gsm="
    elif url_value == 2:
        img_url = "https://pic.sogou.com/pics?query=img_word&mode=1&start=img_page&reqType=ajax&reqFrom=result&tn=0"
    elif url_value == 3:
        img_url = "https://cn.bing.com/images/async?q=img_word&first=img_page&count=35&relp=35&scenario=ImageBasicHover&datsrc=N_I&layout=RowBased_Landscape&mmasync=1&dgState=x*743_y*1322_h*207_c*3_i*71_r*13&IG=F61A2FF509BC4328951A7F1222C8A4B5&SFX=3&iid=images.5633"
    img_url = img_url.replace('img_word', word)
    return img_url


def write_database(file_name):
    image = Image()
    image.path = file_name
    image.save()
    pass


def time_check(time_value, time_list, i):
    # 如果所爬取的网站没有给图片时间信息则返回1
    if len(time_list) == 0:
        return 1

    # 如果用户没有输入时间范围默认爬取全部
    elif len(time_value) == 0:
        return 1

    else:
        st = datetime.strptime(str(time_value[0]), "%Y-%m-%d")
        et = datetime.strptime(str(time_value[1]), "%Y-%m-%d")
        if st < datetime.strptime(time_list[i], "%Y-%m-%d") < et:
            return 1
        else:
            return 0

    pass


def write_file(img_url_list, time_value, time_list):
    img_local = []
    print(time_value)
    image = Image.objects.all()
    i = 0
    flag = 0
    if len(image) != 0:
        flag = int((re.findall(r'\d+', str(image[len(image) - 1].path)))[0]) + 1  # 获取最后一个数值
    cur_path = os.path.abspath(os.path.dirname(__file__)).replace('backer\\service', '')
    for img in img_url_list:
        if time_check(time_value, time_list, i):
            file_name = "img" + str(flag)
            flag += 1
            get_name = file_name + str('.png')
            write_database(get_name)
            file_name = cur_path + str('fonter\\src\\assets\\img\\') + file_name + str('.png')
            img_local.append(get_name)

            with open(file_name, "wb") as f:
                f.write(requests.get(img).content)
        i += 1

    return img_local


# 百度爬虫
def get_baidu_img(url_value, word, time_value):
    for i in range(1, 5):
        img_url = get_url(url_value, word)
        img_url = img_url.replace('img_page', str(i * 30))
        print(img_url)
        response = requests.get(img_url, headers=headers)
        img_url_list = re.findall(r'"middleURL":"(.*?)"', response.text)
        time_list = re.findall(r'"bdImgnewsDate":"(.*?) ', response.text)
        write_file(img_url_list, time_value, time_list)


# 搜狗爬虫
def get_sougou_img(url_value, word, time_value):
    time_list = []
    for i in range(1, 5):
        img_url = get_url(url_value, word)
        img_url = img_url.replace('img_page', str(i * 48))
        print(img_url)
        response = requests.get(img_url, headers=headers)
        img_url_list = re.findall(r'"thumbUrl":"(.*?)"', response.text)
        write_file(img_url_list, time_value, time_list)


#bing 爬虫
def get_bing_img(url_value, word, time_value):
    img_url_list = []
    time_list = []
    for i in range(1, 5):
        img_url = get_url(url_value, word)
        img_url = img_url.replace('img_page', str(i * 39))
        response = requests.get(img_url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        src_list = soup.find_all('img', class_='mimg')
        for src in src_list:
            img_url_list.append(src['src'])
        print(img_url_list)
        write_file(img_url_list, time_value, time_list)
    pass


def run(url_value, word, time_value):
    print(url_value, word)
    img_local = []
    if url_value == 1:
        get_baidu_img(url_value, word, time_value)
    elif url_value == 2:
        get_sougou_img(url_value, word, time_value)
    elif url_value == 3:
        get_bing_img(url_value, word, time_value)
    return img_local


if __name__ == "__main__":
    start_time = '2017-11-12'
    end_time = '2015-03-04'
    dt = datetime.strptime(start_time, "%Y-%m-%d")
    print(dt)
