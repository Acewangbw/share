# _*_ coding: utf-8 _*_
from django.db import models
from users.models.Department import Department

_author_ = 'Ace'
_date_ = '2019-01-16 9:50'

class Role(models.Model):
    role = models.ForeignKey(Department,on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    class Meta:
        verbose_name_plural = '角色表'
    def __str__(self):
        return self.name