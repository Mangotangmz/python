from django.db import models

from DjangoUeditor.models import UEditorField


class AType(models.Model):
    types = models.CharField(max_length=10)  # 类型
    f_typeid = models.IntegerField(null=True)  # 父id

    class Meta:
        db_table = 'article_type'

    def to_dict(self):
        return {
            'id': self.id,
            'types': self.types,
            'article_count': self.article_set.count(),
            'f_typeid': self.f_typeid,
        }


class Article(models.Model):
    title = models.CharField(max_length=30, null=False)  # 文章标题
    types = models.ForeignKey(AType, null=False, on_delete=models.CASCADE)  # 文章分类
    is_show = models.BooleanField(default=False) # 是否展示，False为不展示，True为展示
    is_recommend = models.BooleanField(default=False) # 是否推荐，False为不推荐，True为推荐
    desc = models.CharField(max_length=100, null=True)  # 内容描述
    content = UEditorField()  # 文章内容
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'article'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'types': self.types.types,
            'desc': self.desc,
            'is_show': self.is_show,
            'content': self.content,
            'create_time': self.create_time.strftime('%Y-%m-%d')
        }