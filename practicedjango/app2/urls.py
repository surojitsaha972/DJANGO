from django.urls import path
from app2 import views
urlpatterns=[
    path('',views.practice,name='practice'),
    path('prac/',views.practice1,name='practice1'),
]