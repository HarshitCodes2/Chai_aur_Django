from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("You are at Chai aur Django Home Page")
    return render(request, 'website/index.html')


def about(request):
    # return HttpResponse("You are at Chai aur Django about Page")
    return render(request, 'website/about.html')


def contact(request):
    return HttpResponse("You are at Chai aur Django contact Page")



