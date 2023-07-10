from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from item.models import Category, Item
from  .forms import LoginForm, SignupForm
from django.contrib.auth import logout

# Create your views here.
@login_required
def index(request):
    items=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()

    return render(request, 'core/index.html', {
        'categories':categories,
        'items': items,    
    })

@login_required 
def contact(request):
    return render(request, 'core/contact.html', {})

def signup(request):
    if request.method =='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:  
        form=SignupForm()

    return render(request, 'core/signup.html', {
        'form':form 
    })


def logout_view(request):
    logout(request)
    return redirect('/')