from django.contrib import admin
from django.urls import path, include
from backer import views


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('data/', views.DataTest),
    path('login/', views.login),
    path('register/', views.register),
    path('sendmessage/', views.sendmessage),
    path('reptile/', views.reptile),

    # 数据库增删改查示例
    path('insertPerson/', views.insertPerson),
    path('delPerson/', views.delPerson),
    path('updatePerson/', views.updatePerson),
    path('listPerson/', views.listPerson),

    # 数据标注
    path('getImage/',views.getDataUrl),
    path('transData/',views.saveTransData)
]
