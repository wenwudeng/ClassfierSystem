from django.http import HttpResponse

def DataTest(request):
    print("===========")
    return HttpResponse(['后台列表数据1', '后台列表数据2'])
# Create your views here.

