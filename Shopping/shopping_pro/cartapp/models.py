from django.db import models
from shopping_app.models import product
# Create your models here.
class cart(models.Model):
    cart_id=models.CharField(max_length=250,blank=True)
    date=models.DateField(auto_now_add=True)

    class Meta:
        db_table='cart'
        ordering=['date']

    def __str__(self):
        return self.cart_id

class cartitem(models.Model):
    prod=models.ForeignKey(product,on_delete=models.CASCADE)
    cid=models.ForeignKey(cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table='cartitem'

    def sub_total(self):
        return self.prod.price*self.quantity

    def __str__(self):
        return self.prod.name