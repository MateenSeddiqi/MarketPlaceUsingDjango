from django import forms 

from .models import Item 

class NewItemForm(forms.ModelFOrm):
    class Meta:
        model= Item
        fields= ('category', 'name', 'description', 'price', 'image')