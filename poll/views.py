from django.shortcuts import render
from  django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('This is fucking shit! Take it and don`t cry like a bitch!' )