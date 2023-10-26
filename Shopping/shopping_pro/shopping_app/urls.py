
from django.urls import path
from . import views
app_name='shopping_app'
urlpatterns = [

    path('',views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='pro_by_cat'),
    path('<slug:c_slug>/<slug:p_slug>/',views.proDet,name='proDet')
]