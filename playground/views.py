from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def say_hello(request: HttpRequest):
    return render(request, 'hello.html', {"name": "Ali Ahmad"})
