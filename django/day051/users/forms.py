'''Tangzhuzhu'''
'''
导包规则：
1.先引入python自带的

2.引入第三方

3.引入自定义
'''
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.Form):
    """

    """

    username = forms.CharField(required=True, max_length=5, min_length=2,
                               error_messages=
                               {'required': '用户名必填',
                                'max_lenghth': '用户名不能大于5个字符',
                                'min_lenght': '用户名不能少于2个字符'
                                })
    psssword = forms.CharField(required=True, min_length=6,
                               error_messages={
                                   'required': '密码必填',
                                   'min_length': '密码不能少于六位'
                               })
    password2 = forms.CharField(required=True, min_length=6,
                                error_messages={
                                    'required': '密码必填',
                                    'min_length': '密码不能少于六位'}
                                )

    def clean(self):
        # 校验用户名是否已经注册过

        user = User.objects.filter(username=self.cleaned_data.get('username'))
        if user:
            #             如果用户存在
            raise forms.ValidationError({'username': '用户名存在'})

        #        校验密码是否相等
        if self.cleaned_data.get('password') != self.cleaned_data.get("password2"):
            raise forms.ValidationError({"password": "两次密码不一致"})


class UserLoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=5, min_length=2,
                               error_messages=
                               {'required': '用户名必填',
                                'max_lenghth': '用户名不能大于5个字符',
                                'min_lenght': '用户名不能少于2个字符'
                                })
    psssword = forms.CharField(required=True, min_length=6,
                               error_messages={
                                   'required': '密码必填',
                                   'min_length': '密码不能少于六位'
                               })
    password2 = forms.CharField(required=True, min_length=6,
                                error_messages={
                                    'required': '密码必填',
                                    'min_length': '密码不能少于六位'}
                                )

    def clean(self):
        # 校验用户是否存在
        user = User.objects.filter(username=self.cleaned_data['username'])

        if not user:
            raise forms.ValidationError({'username': '请先注册'})
        return self.cleaned_data
