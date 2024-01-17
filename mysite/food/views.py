
from django.shortcuts import redirect, render

from django.http import HttpResponse
from django.template import loader
from .models import Item

from .forms import ItemForm

# Create your views here.

def index(Request):

    item_list=Item.objects.all()

    context={

        'item_list':item_list,

    }

    return render(Request,'food/index.html',context)


def details(Request,item_id):

    item=Item.objects.get(pk=item_id)

    context={

        "item":item,
    }

    return render(Request,"food/detail.html",context)

def create_item(Request):
    form=ItemForm(Request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')
    
    return render(Request,'food/item-form.html',{'form':form})


def update_item(Request,id):

    item=Item.objects.get(id=id)
    form=ItemForm(Request.POST or None, instance=item)

    if form.is_valid():

        form.save()
        return redirect('index')
    return render(Request,'food/item-form.html',{'form':form,'item':item})


def delete_item(Request,id):
    item=Item.objects.get(id=id)

    if Request.method == 'POST':
        item.delete()
        return redirect('index')
    
    return render(Request,'food/item-delete.html',{'item':item})
