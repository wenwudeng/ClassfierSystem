from django.db import models


# 创建person表
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=20)
    p_age = models.CharField(max_length=3, blank=True)
    p_sex = models.CharField(max_length=10, blank=True)

    # 修改表名
    class Meta:
        db_table = "Person"
