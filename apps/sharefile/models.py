from django.db import models
from datetime import datetime
# from categories.models import CustomerType
from operation.models import FileUsedfor,FileDepartment
from django.utils import timezone

from django.urls import reverse

# Create your models here.

class AddFileModel(models.Model):

    models_Filename = models.CharField(max_length=20, verbose_name=u"文件名称", default='')
    models_Filedepartment = models.CharField(max_length=20, verbose_name=u"BUH", default='')
    # models_Filedepartment = models.ForeignKey(FileDepartment,on_delete=models.CASCADE,verbose_name=u"人数", default='')
    models_Filedes = models.TextField(verbose_name=u"描述", default='')

    models_Fileusedfor = models.CharField(max_length=20, verbose_name=u"人数", default='')
    # models_Fileusedfor = models.ForeignKey(FileUsedfor,on_delete=models.CASCADE,verbose_name=u"人数", default='')
    models_Fileupload = models.FileField(
        upload_to="file/%Y/%m",
        verbose_name=u"文件",
        max_length=1000, )
    models_Updated_date = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    models_clicknum = models.IntegerField(default=0, verbose_name=u"下载次数")

    class Meta:
        verbose_name = u"上传文件"
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[str(self.id)])

    def viewed(self):
        self.models_clicknum += 1
        self.save(update_fields=['models_clicknum'])



#访问网站的ip地址和次数
class Userip(models.Model):
    ip=models.CharField(verbose_name='IP地址',max_length=30)    #ip地址
    count=models.IntegerField(verbose_name='访问次数',default=0) #该ip访问次数
    class Meta:
        verbose_name = '访问用户信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.ip

#网站总访问次数
class VisitNumber(models.Model):
    count=models.IntegerField(verbose_name='网站访问总次数',default=0) #网站访问总次数
    class Meta:
        verbose_name = '网站访问总次数'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.count)

#单日访问量统计
class DayNumber(models.Model):
    day=models.DateField(verbose_name='日期',default=timezone.now)
    count=models.IntegerField(verbose_name='网站访问次数',default=0) #网站访问总次数
    class Meta:
        verbose_name = '网站日访问量统计'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.day)



