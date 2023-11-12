from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView

from .forms import fo
from .models import too


# Create your views here.

class home(ListView):
    model=too
    template_name = 'index.html'
    context_object_name = 'obj'

class det(DetailView):
    model = too
    template_name = 'detail.html'
    context_object_name = 'tas'

class up(UpdateView):
    model = too
    template_name = ''
def index(request):
    obj=too.objects.all()
    if request.method=='POST':
        name=request.POST.get('ent',)
        priority=request.POST.get('prior',)
        date=request.POST.get('date',)
        new=too(name=name,priority=priority,date=date)
        new.save()
        return redirect('/')

    return render(request,'index.html',{'obj':obj})

def delete(request,id):
    tas = too.objects.get(id=id)
    if request.method=='POST':

       tas.delete()
       return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    tas=too.objects.get(id=id)
    f=fo(request.POST or None,instance=tas)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'update.html',{'task':tas,'form':f})
