from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fashion_blog(request):
    return HttpResponse("Fashion Tech Blog!")