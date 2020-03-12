from django.contrib import admin
from .models import BlogType, Blog, ReadNum


# Register your models here.
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'blog_type', 'getReadNum' , 'created_time', 'last_updated_time')


@admin.register(ReadNum)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog', 'read_num')
