from django.shortcuts import render
from item.models import Category, Item

# Create your views here.
def index(request):
    categories=Category.objects.all()
    return render(request, 'core/index.html', {'categories':categories})

def contact(request):
    return render(request, 'core/contact.html', {})
