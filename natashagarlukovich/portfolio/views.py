from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
 
from  portfolio.models import Image, Logo
 
 
def portfolio(request):
	imageList = Image.objects.filter(visible='1')

	logoList = Logo.objects.all()

	context = {
		"imageList": imageList,
		"logoList": logoList,
    }

	return render(request, "partial/portfolio.html", context)