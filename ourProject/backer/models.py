from django.db import models


# 创建user表
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=11)
    password = models.CharField(max_length=20)
    type = models.CharField(max_length=20)

    # 修改表名
    class Meta:
        db_table = "T_User"


# 创建图片表
class Image(models.Model):
    id = models.AutoField(primary_key=True)  # 键
    path = models.CharField(max_length=100)  # 图片路径
    isTrue = models.BooleanField(default=False)  # Boolean判断,

    # 修改表名
    class Meta:
        db_table = "T_Image"


# 创建person表，用于测试
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=20)
    p_age = models.CharField(max_length=3, blank=True)
    p_sex = models.CharField(max_length=10, blank=True)

    # 修改表名
    class Meta:
        db_table = "Person"


