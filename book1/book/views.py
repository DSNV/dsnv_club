from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView


def index(request):
    return render(request, 'dsnv_club/index.html', locals())


def base(request):
    return render(request, 'base.html', locals())

