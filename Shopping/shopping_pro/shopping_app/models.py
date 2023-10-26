from django.db import models
from django.urls import reverse


# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=200,unique=True)
    desc=models.TextField(blank=True)
    image=models.ImageField(upload_to='category')
    slug=models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering=['name']
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('shopping_app:pro_by_cat',args=(self.slug,))

    def __str__(self):
        return self.name

class product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    image = models.ImageField(upload_to='product')
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    stock=models.IntegerField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    available=models.BooleanField()
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['name']
        verbose_name='product'
        verbose_name_plural='products'

    def get_url(self):
        return reverse('shopping_app:proDet',args=(self.category.slug,self.slug,))

    def __str__(self):
            return self.name