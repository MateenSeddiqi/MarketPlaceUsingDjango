from django import path

from . import views
app_name='conversation'

urlpattern=[
    path('new/<int:item_pk>/', views.new_conversation, name='new '),
]