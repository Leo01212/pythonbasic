from django.shortcuts import render, get_object_or_404

from .models import category,product
from django.core.paginator import InvalidPage,EmptyPage,Paginator
# Create your views here.
def home(request,c_slug=None):
    c_page=None
    product_list=None
    if c_slug!=None:
        c_page=get_object_or_404(category,slug=c_slug)
        product_list=product.objects.all().filter(category=c_page,available=True)
    else:
        product_list = product.objects.all().filter(available=True)
    pagein=Paginator(product_list,6)
    try:
        pag=int(request.GET.get('page',1))
    except:
        pag=1
    try:
        products=pagein.page(pag)
    except (EmptyPage,InvalidPage):
        products = pagein.page(pagein.num_pages)
    return render(request,'category.html',{'category':c_page,'products':products})

def proDet(request,c_slug,p_slug):
    try:
        pro=product.objects.get(category__slug=c_slug,slug=p_slug)
    except Exception as e:
        raise e

    return render(request,'product.html',{'pro':pro})