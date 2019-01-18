from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import View
from users.models import User2Role, Permission, UserProfile
from .models import AddFileModel,FileUsedfor
from .forms import AddfileForms
from datetime import datetime
from users.models.Dep import Dep

from django.shortcuts import render_to_response

from .cunt import change_info
# Create your views here.

from utils.mixin_utils import LoginRequiredMixin



class AddfileView(LoginRequiredMixin,View):
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self,request):
        dept = Dep.objects.all()
        usedfor = FileUsedfor.objects.all()

        return render(request,'Ace-file-add-realestate-add-property.html',{
            'dept':dept,
            'usedfor': usedfor,
        })

    def post(self,request):
        addfile_form = AddfileForms(request.POST)

        file_profile = AddFileModel()

        if addfile_form.is_valid():
            file_profile.models_Filename = request.POST.get("filename", "")
            file_profile.models_Filedepartment = request.POST.get("filedepartment", "")
            file_profile.models_Filedes = request.POST.get("filedes", "")
            file_profile.models_Fileusedfor = request.POST.get("fileusedfor", "")


            if 'fileupload' in list(request.FILES.keys()):
                file_profile.models_Fileupload = request.FILES['fileupload']


            file_profile.models_Updated_date = datetime.now()
            # 保存
            file_profile.save()

            return redirect('/sharefile/filelist/')

        else:
            return render(request, 'Ace-file-add-realestate-add-property.html')


# status = ''
class FileListView(LoginRequiredMixin,View):
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self,request):
        #从session获取用户信息
        user = request.session.get("user")
        user_name = user.get("user_name")
        #查询对应用户信息
        user_obj = UserProfile.objects.filter(email=user_name)[0]
        #部门id
        dep_id = user_obj.department_id
        dep_name = user_obj.department.Department_name
        #查询部门对应的文件
        allfile = AddFileModel.objects.filter(models_Filedepartment=dep_name)
        # allfile = AddFileModel.objects.filter(department_id=dep_id)
        print("8"*10)
        print(allfile)
        #allfile = AddFileModel.objects.all()
       # countfile = AddFileModel.objects.count()
        countfile = len(allfile)

        # user_obj = UserProfile.objects.get(username=username)

        return render(request,'Ace-filelist-transaction-listing.html',{
            'allfile':allfile,
            'countfile':countfile
        })

    def post(self,request):

        file_id = request.POST['file_id'] #找到对应文件的ID。
        op = request.POST['op'] #找到前端中标记出来的操作。
        if 'del' == op: #找寻操作用，可以用于区别编辑内容。
            try:
                r = AddFileModel.objects.filter(id=int(file_id))#筛选出ID。
                r.delete()#删除
                # global status
                # status = 'del success'
                return redirect('/sharefile/filelist/')
            except:
                # global status
                # status = 'del failed'
                return redirect('/sharefile/filelist/')
                pass

        return redirect('/sharefile/filelist/')


class CountDownloadView(View):
    def get(self,request,file_id):
        count = AddFileModel.objects()
        countfile = AddFileModel.objects.get(id=int(file_id))
        countfile.models_clicknum += 1
        countfile.save()
        return render(request,'Ace-filelist-transaction-listing.html',{
            'count':count,
        })



def del_file(request):
        file_id = request.POST['file_id']
        try:
            file = AddFileModel.objects.get(id=int(file_id))
            file.delete()
            return HttpResponse('1')
        except:
            return HttpResponse('2')


# class DeleteFile(View):
#     def get(self,request,file_id):
#         file_delete = AddFileModel.objects.get(id=int(file_id))
#         file_delete.delete()
#         return render(request, 'Ace-filelist-transaction-listing.html', {
#             'file_delete': file_delete,
#         })

    # def del_article(request):
    #     file_id = request.POST['file_id']
    #     try:
    #         article = AddFileModel.objects.get(id=file_id)
    #         article.delete()
    #         # return HttpResponse("1")
    #         return redirect('/sharefile/filelist')
    #     except:
    #         # return HttpResponse("2")
    #         return redirect('/sharefile/filelist')



class ButtonsView(View):
    def get(self,request):
        return render(request,'Tools-anybuttons-ui-buttons.html')

class EditView(View):
    def get(self,request):
        return render(request,'Tools-edit-table-jsgrid.html')

class WheelView(View):
    def get(self,request):
        return render(request,'Tools-wheel-widget-data.html')

