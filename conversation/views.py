from django.shortcuts import render, get_object_or_404, redirect
from items.models import Item
from .models import Conversation
from .forms import ConversationMessage

# Create your views here.

def new_conversation(request, item_pk):
    item=get_object_or_404(Item, pk=item_pk)
    if item.created_by == request.user:
        return redirect('dashboard:index')
    conversations=Conversation.objects.filter(item==item).filter(members__in=[request.user.id])

