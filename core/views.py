from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, soma, n1, n2 ):
    result = n1 + n2
    return HttpResponse('<h1>hello {} a soma de {} e {} é {} = {}</h1>'.format(nome, n1, n2 , soma, result))
