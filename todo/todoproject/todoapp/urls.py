from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path('',views.index,name='index'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('home/',views.home.as_view(),name='home'),
    path('detail/<int:pk>/', views.det.as_view(), name='detail'),
]