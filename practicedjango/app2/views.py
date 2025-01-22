from django.shortcuts import render
from django.http import HttpResponse
def practice(request):
    return HttpResponse("Hello User!")
def practice1(request):
    return render(request,"1st.html")
# Create your views here.