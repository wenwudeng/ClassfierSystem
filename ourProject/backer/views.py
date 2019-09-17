from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random
import re

from .service import reptiles
from . import zhenzismsclient as smsclient

from .models import *


def DataTest(request):
    print("===========")
    return HttpResponse(['后台列表数据1', '后台列表数据2'])


num = ''

def code(n=6, alpha=True):
    s = '' # 创建字符串变量,存储生成的验证码
    for i in range(n):  # 通过for循环控制验证码位数
        num = random.randint(0, 9)  # 生成随机数字0-9
        if alpha: # 需要字母验证码,不用传参,如果不需要字母的,关键字alpha=False
            upper_alpha = chr(random.randint(65, 90))
            lower_alpha = chr(random.randint(97, 122))
            num = random.choice([num, upper_alpha, lower_alpha])
        s = s + str(num)
    return s


@csrf_exempt
def sendmessage(request):
    data = {}
    username = json.load(request).get('username')

    ret = re.match(r"^1[35678]\d{9}$", username)
    if ret is None:
        data['errno'] = 405
        data['msg'] = '请输入正确的手机号'
        return JsonResponse(data)

    client = smsclient.ZhenziSmsClient("https://sms_developer.zhenzikj.com", "102561",
                                       "3d8791f5-8cfa-4468-b9e7-13cb5b3f0ef8")
    global num
    num = str(code(6, False))
    client.send(username, '您的验证码为：' + num)
    data['errno'] = 200
    data['msg'] = '发送成功'
    return JsonResponse(data)


@csrf_exempt
def login(request):
    # request是WSGIRequest类型
    form = json.load(request)
    form = form.get('form')
    data = {}
    # 如果数据库没有，则user为None
    user = User.objects.filter(username=form.get('username'), password=form.get('password')).first()
    print(user)
    if (user is not None):
        data['errno'] = 200
        data['msg'] = '登录成功'
        data['role'] = user.type
    else:
        data['errno'] = 405
        data['msg'] = '账号或密码错误'

    return JsonResponse(data)


@csrf_exempt
def register(request):
    form = json.load(request)
    form = form.get('form')
    data = {}

    # 如果数据库没有，则user为None
    user = User.objects.filter(username=form.get('username')).first()
    if (user is not None):
        data['errno'] = 405
        data['msg'] = '用户名或手机号已经注册'
        return JsonResponse(data)

    global num
    if (num != form.get('verification')):
        data['errno'] = 405
        data['msg'] = '验证码错误'
        return JsonResponse(data)
    # 验证码置空
    num = ''

    user = User()
    user.username = form.get('username')
    user.password = form.get('password')
    user.type = form.get('role')
    user.save()

    data['errno'] = 200
    data['msg'] = '注册成功'
    return JsonResponse(data)


# 增
def insertPerson(request):
    # 创建一个对象
    person = Person()
    # 设置属性
    person.p_name = "王" + str(random.randint(1, 100))
    person.p_age = random.randint(1, 100)
    person.p_sex = random.randint(0, 1)
    # 保存数据
    person.save()
    return HttpResponse("插入成功")


# 删
def delPerson(request):
    id = 2
    person = Person.objects.filter(id=id)  # 用变量person接收获取到的对象
    person.delete()
    return HttpResponse("删除成功")


# 改
def updatePerson(request):
    id = 1
    person = Person.objects.filter(id=id).first()
    person.p_name = "王小明"
    person.p_age = 18
    person.p_sex = 0
    person.save()
    return HttpResponse("修改成功")


# 查
def listPerson(request):
    persons = Person.objects.all()
    for item in persons:
        print(item.id)

    # 可以使用JsonResponse返回json数据到前端
    return HttpResponse("查询成功")


# 爬虫
@csrf_exempt
def reptile(request):
    result = []
    date = json.load(request)
    print(date)
    url_value = int(date.get('url_value'))
    word = date.get('word')
    reptiles.run(url_value, word)
    data = {}
    print(data)
    return JsonResponse(data)


# 获取图片
@csrf_exempt
def get_img(request):
    images = Image.objects.all()
    img_local = []
    for item in images:
        img_local.append(item.path)
    # data = json.loads(img_local)
    length = len(img_local)
    img_local = img_local[length - 8: length]
    data = {"img_local": img_local}
    return JsonResponse(data)
    pass
