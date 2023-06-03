from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def kittu(request):
    return Httpresponse('<h1>this is specific url mapping<h1>')