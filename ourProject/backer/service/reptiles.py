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
        img_url =  "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=img_word&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=img_word&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=img_page&rn=30&gsm=&1568222792994="
    elif url_value == 2:
        img_url = "https://pic.sogou.com/pics?query=img_word&mode=1&start=img_word&reqType=ajax&reqFrom=result&tn=0"
    img_url = img_url.replace('img_word', word)
    return img_url


def get_new_name(file_name):
    file_name = file_name.replace('<', '')
    file_name = file_name.replace('>', '')
    file_name = file_name.replace('《', '')
    file_name = file_name.replace('》', '')
    file_name = file_name.replace('\\', '')
    file_name = file_name.replace('?', '')
    file_name = file_name.replace('|', '')
    file_name = file_name.replace('!', '')
    file_name = file_name.replace(':', '')
    if file_name == '':
        file_name = 'temp'
    return file_name


def write_database(file_name):
    image = Image()
    image.path = file_name
    image.save()
    pass


def write_file(img_url_list, img_name):
    img_local = []
    get_name = []
    flag = 0
    cur_path = os.path.abspath(os.path.dirname(__file__)).replace('backer\\service', '')
    for img in img_url_list:
        file_name = img_name[flag]
        flag += 1
        file_name = get_new_name(file_name)
        get_name = file_name + str('.png')
        database_name = str('fonter\\src\\assets\\img\\') + file_name + str('.png')
        file_name = cur_path + str('fonter\\src\\assets\\img\\') + file_name + str('.png')
        img_local.append(get_name)
        write_database(database_name)
        with open(file_name, "wb") as f:
            f.write(requests.get(img).content)
    return img_local


# 百度爬虫
def get_baidu_img(url_value, word):
    img_url = get_url(url_value, word)
    img_local = []
    for i in range(1, 2):
        img_url = img_url.replace('img_page', str(i * 30))
        response = requests.get(img_url, headers=headers)
        img_url_list = re.findall(r'"middleURL":"(.*?)"', response.text)
        img_name = re.findall(r'"fromPageTitleEnc":"(.*?)"', response.text)
        img_local = write_file(img_url_list, img_name)
    return img_local


# 搜狗爬虫
def get_sougou_img(url_value, word):
    img_url = get_url(url_value, word)
    img_local = []
    for i in range(1, 2):
        img_url = img_url.replace('img_page', str(i * 48))
        response = requests.get(img_url, headers=headers)
        img_url_list = re.findall(r'"thumbUrl":"(.*?)"', response.text)
        img_name = re.findall(r'"title":"(.*?)"', response.text)
        img_local = write_file(img_url_list, img_name)
    return img_local


def run(url_value, word):
    print(url_value, word)
    img_local = []
    if url_value == 1:
        print('in')
        img_local = get_baidu_img(url_value, word)
    elif url_value == 2:
        img_local = get_sougou_img(url_value, word)
    return img_local


if __name__ == "__main__":
    run(2, "羊")
