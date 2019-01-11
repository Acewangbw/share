# encoding: utf-8
from users.models import UserProfile

__author__ = 'mtianyan'
__date__ = '2018/1/10 0010 05:56'

# 引入Django表单
from  django import forms

# 引入验证码field
from captcha.fields import CaptchaField

# 登录表单验证
class LoginForm(forms.Form):
    # 用户名密码不能为空
    username = forms.CharField(required=True)
    # 密码不能小于5位
    password = forms.CharField(required=True, min_length=5)

# 验证码form & 注册表单form
class RegisterForm(forms.Form):
    # 此处email与前端name需保持一致。
    email = forms.EmailField(required=True)
    # 密码不能小于5位
    password = forms.CharField(required=True, min_length=5)
    # 应用验证码 自定义错误输出key必须与异常一样
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


# 激活时验证码实现
class ActiveForm(forms.Form):
    # 激活时不对邮箱密码做验证
    # 应用验证码 自定义错误输出key必须与异常一样
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


# 忘记密码实现,这个是在点击忘记密码后要填写表单地方可以设定的提醒
class ForgetForm(forms.Form):
    # 此处email与前端name需保持一致。
    emailforget = forms.EmailField(required=True)
    # 应用验证码 自定义错误输出key必须与异常一样, 这里没设定
    # captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


# 重置密码form实现，这里是在点击邮件里面的链接后，跳转到修改密码页面里面需要填写表单的提醒
class ModifyPwdForm(forms.Form):
    # 密码不能小于5位
    password1 = forms.CharField(required=True, min_length=5)
    # 密码不能小于5位
    password2 = forms.CharField(required=True, min_length=5)