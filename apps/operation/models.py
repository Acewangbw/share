# _*_ coding: utf-8 _*_
from django.db import models
from datetime import datetime


from users.models import UserProfile


class FileDepartment(models.Model):
    Department = models.CharField(verbose_name=u"部门", max_length=20)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Mate:
        verbose_name = u"部门"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.Department

class FileUsedfor(models.Model):
    Usedfor = models.CharField(verbose_name=u"用于", max_length=20)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Mate:
        verbose_name = u"用于"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.Usedfor