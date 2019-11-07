from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from  blog.models import Post
 
 
def blog(request):
    postList = Post.objects.filter(visible='1')
 
    context = {
        "postList": postList,
        "title": "Главная страница блога",
        "desc": "Описание для главной страницы",
        "key": "ключевые, слова",
    }
    return render(request, "partial/blog.html", context)
 
def single(request, id=None):
    postList = get_object_or_404(Post, id=id)
 
    context = {
        "postList": postList,
    }
    return render(request, "partial/single.html", context)