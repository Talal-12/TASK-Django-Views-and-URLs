from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_home(request):
    return HttpResponse("<h1>Hello, Welcome to my website!</h1>")