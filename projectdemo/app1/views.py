from django.shortcuts import render
from django.http import JsonResponse
# def home(request):
#     return render(request,"index.html")
def index(request):
    # return render(request,"index.html")
    return render(request,"master.html")

def mas1(request):
    return render(request,"abc.html")

def mas2(request):
    return render(request,"xyz.html")

def indexcon(request):
    return render(request,"indexCon.html")

def index2con(request):
    return render(request,"index2Con.html")

def demo(request):
    return render(request,"demo.html",{'a':1234})

def form(request):
    return render(request,"form.html")


def sub(request):
    x=int(request.GET['n1'])
    y=int(request.GET['n2'])
    z=x-y
    return render(request,"form.html",{'sub':z})

def postform(request):
    return render(request,"form2.html")

def sum(request):
    x=int(request.POST['n1'])
    y=int(request.POST['n2'])
    z=x+y
    return render(request,"form2.html",{'sum':z})

def getpostform(request):
    if(request.method=="POST"):
        x=int(request.POST['n1'])
        y=int(request.POST['n2'])
        z=x/y
        return render(request,"getpostform.html",{'div':z})
    else:
        return render(request,"getpostform.html")



# Create your views here.
