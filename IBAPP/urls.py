from os import name
from django.urls import  path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index1', views.index1, name='index1'),
    path('index2', views.index2, name='index2'),
    path('index3', views.index3, name='index3'),
    path('index4', views.index4, name='index4'),
    path('course',views.course,name='course'),
    path('offers',views.offers,name='offers'),
    path('sero',views.education,name='sero'),
    path('about',views.about,name='about')
     #path('admin/',views.Admin,name="admin/"),
  
 ]