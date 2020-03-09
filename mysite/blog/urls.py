from django.urls import path
from .views import blog_list, blog_detail, blogs_with_type

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('<int:blog_pk>', blog_detail, name='blog_detail'),
    path('type/<int:blog_type_pk>', blogs_with_type, name='blogs_with_type'),
]
