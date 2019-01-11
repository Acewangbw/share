from django.db import models
from datetime import datetime
# Create your models here.

class Addcustomer(models.Model):
    addcustomer = models.CharField(verbose_name=u"部门", max_length=20)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Mate:
        verbose_name = u"客户"
        verbose_name_plural = verbose_name