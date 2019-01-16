# _*_ coding: utf-8 _*_
from datetime import datetime
from django.db import models

_author_ = 'Ace'
_date_ = '2019-01-16 9:42'


# 部门
class Department(models.Model):
    Department = models.CharField(verbose_name=u"部门", max_length=20,default='All')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Mate:
        verbose_name = u"部门"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.Department
