from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'shopup/index.html')


def create(request):
    return render(request, 'shopup/create.html')


def scrapper(request):
    context = get_response(request.product_link)
    return render(request, 'shopup/result.html', context)

