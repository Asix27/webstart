from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(requset):
    return render(requset,'main/about.html')