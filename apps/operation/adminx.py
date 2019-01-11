# encoding: utf-8
_author_ = 'Ace'
_date_ = '2019-01-08 12:26'
import xadmin
from .models import FileDepartment,FileUsedfor


class FileDepartmentAdmin(object):
    list_display = ['Department', 'add_time']

    search_fields = ['Department', 'add_time']

    list_filter = ['Department', 'add_time']


xadmin.site.register(FileDepartment, FileDepartmentAdmin)

class FileUsedforAdmin(object):
    list_display = ['Usedfor', 'add_time']

    search_fields = ['Usedfor', 'add_time']

    list_filter = ['Usedfor', 'add_time']


xadmin.site.register(FileUsedfor, FileUsedforAdmin)