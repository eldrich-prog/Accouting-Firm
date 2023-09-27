from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse


def index(request):

     return render(request, "accouting/index.html")

    #return HttpResponse("Hello, world. Este es el index de la firma contable.")

