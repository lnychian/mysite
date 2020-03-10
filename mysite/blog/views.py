from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
# Create your views here.
from .models import Blog, BlogType


def blog_list(request):
    blogs_all_list = Blog.objects.all()
    paginator = Paginator(blogs_all_list,3)#每3页进行分页
    page_num =  request.GET.get('page',1)#获取url的页面参数(GET请求)
    page_of_blogs = paginator.get_page(page_num)

    context = {}
    context['page_of_blogs'] = page_of_blogs
    context['blog_types'] = BlogType.objects.all()
    return render(request, '../templates/blog_list.html', context)


def blog_detail(request, blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog, pk=blog_pk)
    return render(request, '../templates/blog_detail.html', context)


def blogs_with_type(request, blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    context['blog_types'] = BlogType.objects.all()
    return render(request, '../templates/blogs_with_type.html', context)
