from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
 
from  about.models import Post
from  portfolio.models import Logo
 
 
def about(request):
	logoList = Logo.objects.all()
	postList = Post.objects.all()

	context = {
		"logoList": logoList,
		"postList": postList,
	}
	return render(request, "partial/about.html", context)