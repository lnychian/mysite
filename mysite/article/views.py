from django.shortcuts import render, get_object_or_404
from .models import Article


# Create your views here.
def acticle_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {}
    context['article_obj'] = article

    return render(request, '../templates/article_detail.html', context)


def acticle_list(request):
    articles = Article.objects.all()
    context = {}
    context['articles'] = articles

    return render(request, '../templates/article_list.html', context)
