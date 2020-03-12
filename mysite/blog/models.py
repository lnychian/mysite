from django.contrib.auth.models import User
from django.core import exceptions
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name


class Blog(models.Model):
    title = models.CharField(max_length=30)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Blog: %s>' % self.title

    def getReadNum(self):
        try:
            return self.readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0

    class Meta:
        ordering = ['created_time']


class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    blog = models.OneToOneField(Blog, on_delete=models.DO_NOTHING)
