from django.shortcuts import render
from django.http.response import Http404, HttpResponse
from .models import Product
# Create your views here.


def index(request):
    
    prodls=Product.objects.all()
    print(prodls)

    return render(request, 'index.html',{'prodls': prodls}) 