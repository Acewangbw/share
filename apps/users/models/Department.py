# _*_ coding: utf-8 _*_
from datetime import datetime
from django.db import models

from users.models.UserProfile import UserProfile

_author_ = 'Ace'
_date_ = '2019-01-16 9:42'


# 部门 1
class Department(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    Department_name = models.CharField(verbose_name=u"部门", max_length=20)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Mate:
        verbose_name_plural = u"部门"

    def __unicode__(self):
        return self.Department_name
