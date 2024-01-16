from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Category
from .forms import NewItemForm, EditItemForm
from django.db.models import Q

@login_required 
def details(request, pk):
    item=get_object_or_404(Item, pk=pk)
    related_items=Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]
    return render (request, 'item/details.html', {
        'item':item,
        'related_items':related_items,
    })

@login_required  
def NewItem(request):
    if request.method=='POST':
        form=NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()
            return redirect('item:details', pk=item.id)
    
    else:
        form = NewItemForm()
    return render(request, 'item/form.html', {
        'form':form,
        'title': 'New item',
    })

@login_required
def delete(request, pk):
    item =get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')

@login_required  
def EditItem(request, pk):
    item =get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method=='POST':
        editItemForm=EditItemForm(request.POST, request.FILES, instance=item)
        if editItemForm.is_valid():
            editItemForm.save()
            return redirect('item:details', pk=item.id)
    else:
        editItemForm = EditItemForm(instance=item)
    return render(request, 'item/form.html', {
        'editItemForm':editItemForm,
        'title': 'Edit item',
    })

@login_required  
def items(request):
    query= request.GET.get('query', '')
    category_id=request.GET.get('category', 0)
    categories=Category.objects.all()
    items=Item.objects.filter(is_sold=False)
    if category_id:
        items=items.filter(category_id=category_id)
    if query:
        items=items.filter (Q(name__icontains=query)) 

    return render (request, 'item/items.html', {
        'items':items,
        'query':query,
        'categories':categories,
        'category_id':int(category_id) 
    }) 