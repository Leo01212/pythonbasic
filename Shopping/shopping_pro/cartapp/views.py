from django.shortcuts import render, redirect
from shopping_app.models import product
from .models import cart,cartitem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def cart__id(request):
    cart__id=request.session.session_key
    if not cart__id:
        cart__id=request.session.create()
    return  cart__id


def add_cart(request,pro_id):

    products=product.objects.get(id=pro_id)
    try:
        Cart=cart.objects.get(cart_id=cart__id(request))
    except cart.DoesNotExist:
        Cart=cart.objects.create(cart_id=cart__id(request))
        Cart.save()
    try:
        cart_item=cartitem.objects.get(cid=Cart,prod=products)
        if cart_item.quantity < cart_item.prod.stock:
            cart_item.quantity+=1
            cart_item.save()
    except cartitem.DoesNotExist:

        cart_item=cartitem.objects.create(prod=products,cid=Cart,quantity=1)
        cart_item.save()
    return redirect('cartapp:cart_detail')

def cart_detail(request,cart_item=None,total=0,encounter=0):
    try:
        carts=cart.objects.get(cart_id=cart__id(request))
        cart_item=cartitem.objects.filter(cid=carts,active=True)
        for i in cart_item:
            total+=i.prod.price*i.quantity
            encounter+=1
    except ObjectDoesNotExist:
        pass
    return render(request,'cart_detail.html',{'cart_item':cart_item,'total':total,'encounter':encounter})

def remove(request,pro_id):
    products = product.objects.get(id=pro_id)
    Cart = cart.objects.get(cart_id=cart__id(request))
    cart_item = cartitem.objects.get(cid=Cart, prod=products)
    if cart_item.quantity >1:
        cart_item.quantity-=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cartapp:cart_detail')

def delete(request,pro_id):
    products = product.objects.get(id=pro_id)
    Cart = cart.objects.get(cart_id=cart__id(request))
    cart_item = cartitem.objects.get(cid=Cart, prod=products)
    cart_item.delete()
    return redirect('cartapp:cart_detail')