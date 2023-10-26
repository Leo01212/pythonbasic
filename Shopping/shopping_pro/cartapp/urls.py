from django.urls import path
from . import views
app_name='cartapp'
urlpatterns = [
    path('add/<int:pro_id>/',views.add_cart,name='add_cart'),
    path('',views.cart_detail,name='cart_detail'),
    path('remove/<int:pro_id>/',views.remove,name='remove'),
    path('delete/<int:pro_id>/',views.delete,name='delete')

]