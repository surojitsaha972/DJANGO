# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("About Surojit Saha")
    s={'name':'Surojit Saha','place':'Durgapur'}
    return render(request, 'index.html',s)

def about(request):
    return HttpResponse("About Surojit Saha")

def htmlstyle(request):
    return HttpResponse("<h1><b>About Surojit Saha</b></h1> <a href='/'>Back</a>")

def openbyurl(request):
    return HttpResponse('''<a href="https://www.youtube.com/"><b>YouTube</b></a>''')

