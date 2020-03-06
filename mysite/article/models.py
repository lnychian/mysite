from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30, db_column='标题')
    content = models.TextField(db_column='文章内容')
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    is_deleted = models.BooleanField(default=False)
    readed = models.IntegerField(default=0)

    def __str__(self):
        return '<Article: %s>' % self.title
