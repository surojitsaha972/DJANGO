# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("About Surojit Saha")
    s={'name':'Surojit Saha','place':'Durgapur'}
    return render(request, 'index.html',s)

def about(request):
    return HttpResponse("About Surojit Saha")

def analyze(request):
    # get the text
    texttype=request.GET.get('text','default')
    yt=request.GET.get('analyze','off')
    print(texttype)
    print(yt)
    # analyze the text
    analyzed=texttype
    p={'purpose':'Analyzing Text','analyzed_text':analyzed}
    return render(request,'analyze.html',p)

def htmlstyle(request):
    return HttpResponse("<h1><b>About Surojit Saha</b></h1> <a href='/'>Back</a>")

# def openbyurl(request):
#     # get the text
#     texttype=request.GET.get('text','default')
#     yt=request.GET.get('youtube','off')
#     print(texttype)
#     print(yt)
#     # analyze the text
#     return HttpResponse('''<a href="https://www.youtube.com/"><b>YouTube</b></a>''')

