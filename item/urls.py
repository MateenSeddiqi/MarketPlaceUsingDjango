from django.urls import path
from . import views
app_name='item'

urlpatterns=[
    path('<int:pk>/', views.details, name='details'),
    path('new/', views.new, name="new"), 
]