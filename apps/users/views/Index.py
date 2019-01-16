# _*_ coding: utf-8 _*_
from django.shortcuts import render

# 基于类实现需要继承的view
from django.views.generic.base import View

from sharefile.models import AddFileModel


class Index(View):
    def get(self,request):
        allfile = AddFileModel.objects.all()
        return render(request, 'Ace-dashboard-table-basic.html', {
                'allfile': allfile,
            })