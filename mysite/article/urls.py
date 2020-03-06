from django.urls import path
from .views import acticle_detail, acticle_list

urlpatterns = [
    path('', acticle_list, name='acticle_list'),
    path('<int:article_id>', acticle_detail, name='acticle_detail'),
]
