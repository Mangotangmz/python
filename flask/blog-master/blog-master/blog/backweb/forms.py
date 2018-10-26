
from django import forms
from django.contrib.auth.models import User

from backweb.models import Article, AType


class UserLoginForm(forms.Form):
    username = forms.CharField(required=True, error_messages={'required': '用户名必填'})
    password = forms.CharField(required=True, error_messages={'required': '密码必填'})

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username)
        if not user:
            raise forms.ValidationError('用户名不存在')
        else:
            return username


class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=30, required=True, error_messages={'required': '文章标题必填'})
    types = forms.IntegerField(required=True, error_messages={'required': '文章语言类型必填'})
    desc = forms.CharField(max_length=100, required=True, error_messages={'required': '文章副标题必填'})
    content = forms.Textarea()

    class Meta:
        model = Article
        fields = '__all__'

    def clean_types(self):
        """
        通过表单保存数据的时候，会提示types字段必须是AType的对象，但是页面中传递的types是id，而不是对象
        所以通过clean_types方法来返回AType的对象
        :return: AType的对象
        """
        types_id = self.cleaned_data['types']
        types = AType.objects.filter(id=types_id).first()
        return types


class UserChangePwdForm(forms.Form):

    passwd1 = forms.CharField(required=True)
    passwd2 = forms.CharField(required=True)

    def clean(self):
        passwd1 = self.cleaned_data.get('passwd1')
        passwd2 = self.cleaned_data.get('passwd2')
        if not passwd1:
            raise forms.ValidationError('密码必填')
        if not passwd2:
            raise forms.ValidationError('确认密码必填')
        if passwd2 != passwd1:
            raise forms.ValidationError({'passwd2': '两次密码不一致'})
        return passwd1

