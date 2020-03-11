from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog, BlogType


# Create your views here.


# 通用返回参数
def getBlogCommonList(request, blogs_all_list):
    context = {}
    paginator = Paginator(blogs_all_list, 10)  # 每10篇文章进行一次分页
    page_num = request.GET.get('page', 1)  # 获取url的页面参数(GET请求)
    context['page_of_blogs'] = paginator.get_page(page_num)
    blog_types = BlogType.objects.all()
    # blog_types_list = []
    # for blog_type in blog_types:
    #     blog_type.count = Blog.objects.filter(blog_type=blog_type).count
    #     blog_types_list.append(blog_type)
    context['blog_types'] = BlogType.objects.annotate(count=Count('blog'))
    blog_dates_dic = {}
    blog_dates = Blog.objects.dates('created_time', 'month', order='ASC')
    for blog_date in blog_dates:
        blog_dates_dic[blog_date] = Blog.objects.filter(created_time__year=blog_date.year,
                                                        created_time__month=blog_date.month).count()
    context['blog_dates'] = blog_dates_dic
    return context


# 全部博客列表请求
def blog_list(request):
    blogs_all_list = Blog.objects.all()
    context = getBlogCommonList(request, blogs_all_list)
    return render(request, '../templates/blog_list.html', context)


# 同type博客页面请求
def blogs_with_type(request, blog_type_pk):
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
    context = getBlogCommonList(request, blogs_all_list)
    context['blog_type'] = blog_type
    return render(request, '../templates/blogs_with_type.html', context)


# 日期归档页面请求
def blogs_with_date(request, year, month):
    blogs_all_list = Blog.objects.filter(created_time__year=year, created_time__month=month)
    context = getBlogCommonList(request, blogs_all_list)
    context['blogs_with_date'] = '%s年%s月' % (year, month)
    return render(request, '../templates/blogs_with_date.html', context)


# 单篇博客页面请求
def blog_detail(request, blog_pk):
    context = {}
    blog = get_object_or_404(Blog, pk=blog_pk)
    previous_blog = Blog.objects.filter(created_time__lt=blog.created_time).last()
    next_blog = Blog.objects.filter(created_time__gt=blog.created_time).first()
    context['blog'] = blog
    context['previous_blog'] = previous_blog
    context['next_blog'] = next_blog
    return render(request, '../templates/blog_detail.html', context)
