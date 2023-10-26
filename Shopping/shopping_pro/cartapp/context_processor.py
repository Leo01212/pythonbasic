from .models import cart,cartitem
from .views import cart__id
from django.core.exceptions import ObjectDoesNotExist
def counter(request):
    itemcount=0
    if 'admin' in request.path:
        return {}
    else:

        try:
            carts=cart.objects.filter(cart_id=cart__id(request))
            cart_item=cartitem.objects.all().filter(cid=carts[:1])
            for i in cart_item:
                itemcount+=i.quantity
        except cart.DoesNotExist:
            itemcount=0

    return dict(itemcount=itemcount)

