from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
    # return HttpResponse('Hello World')
    return render(request, 'hello.html', {'numbers': [1, 2, 3, 4]})
