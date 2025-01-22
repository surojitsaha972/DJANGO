from django.urls import path
from app1 import views
urlpatterns = [
    # path('amiAdmin/', views.home, name = "Admin"),
    # path('', views.home, name = "Admin"),
    # path('index',views.index,name="Admin"),
    path('master',views.index,name="Admin"),
    path('mas1',views.mas1),
    path('mas2',views.mas2),
    
    path('indexC',views.indexcon),
    
    path('indexCon',views.index2con),
    
    path('demo',views.demo),
    
    path('form',views.form),
    path('sub',views.sub),
    
    path('form2',views.postform),
    path('sum',views.sum),
    
    path('getpostform',views.getpostform),
    
]