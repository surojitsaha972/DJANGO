# I am created this file
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello")
