from django.shortcuts import render
from shopping_app.models import product,category
from django.db.models import Q
# Create your views here.
def search(request):
    query=None
    products=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=product.objects.all().filter(Q(name__contains=query))
    return render(request,'search.html',{'products':products,'query':query})