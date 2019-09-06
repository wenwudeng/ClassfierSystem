from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def DataTest(request):
    print("===========")
    return HttpResponse(['后台列表数据1', '后台列表数据2'])


@csrf_exempt
def login(request):
    # request是WSGIRequest类型
    user = json.load(request)
    username = user.get('username')
    password = user.get('password')
    data = {}
    if (username=='admin' and password=='123'):
        data['errno'] = 200
        data['msg'] = '登录成功'
    else:
        data['errno'] = 405
        data['msg'] = '账号或密码错误'

    return JsonResponse(data)
