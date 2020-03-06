from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30,db_column='标题')
    content = models.TextField(db_column='文章内容')
