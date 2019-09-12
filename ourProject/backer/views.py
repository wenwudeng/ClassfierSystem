from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random

from .models import *


def DataTest(request):
    print("===========")
    return HttpResponse(['后台列表数据1', '后台列表数据2'])


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
    print(form)
    data = {}
    # 如果数据库没有，则user为None
    user = User.objects.filter(username=form.get('username')).first()

    if (user is not None):
        data['errno'] = 405
        data['msg'] = '用户名或手机号已经注册'
        return JsonResponse(data)

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
