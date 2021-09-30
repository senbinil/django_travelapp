from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Place,News
from django.contrib import auth
# Create your views here.


def demo(request):
    print(request)
    get_data=Place.objects.all()
    get_news=News.objects.all()
    return render(request, 'home.html', {'data': get_data,'news':get_news})


def about(request):
    print(request)
    return render(request, 'about.html')


# def add(req):
#     x = int(req.GET['num1'])
#     y = int(req.GET['num2'])
#     addition = x+y
#     mul = x*y
#     sub = x-y
#     try:
#         div = x/y
#         mod = x % y
#     except Exception as e:
#         div = mod = e

#     return render(req, 'about.html', {'num1':x,'num2':y,'add': addition, 'div': div, 'mod': mod, 'mul': mul, 'sub': sub})
