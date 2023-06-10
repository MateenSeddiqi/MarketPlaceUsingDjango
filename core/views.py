from django.shortcuts import render
from item.models import Category, Item
from  .form import SignupForm

# Create your views here.
def index(request):
    items=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()

    return render(request, 'core/index.html', {
        'categories':categories,
        'items': items,    
    })

def contact(request):
    return render(request, 'core/contact.html', {})

def signup(request):
    form=SignupForm()
    return render(request, 'core/signup.html', {
        'form':form 
    })