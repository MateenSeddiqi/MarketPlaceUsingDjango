from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=200)

    class Meta:
        ordering=('name', )
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name

class Item(models.Model):
    category=models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name =models.CharField(max_length=200)
    description=models.TextField(max_length=255)
    price=models.FloatField()
    image=models.ImageField(upload_to='items_image', blank=True, null=True)
    is_sold=models.BooleanField(default=False)
    created_by= models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# This code is defining a foreign key relationship between two models in Django.
# The first argument, Category, specifies the model that this foreign key is relating to. The related_name argument specifies the name of the reverse relation from the related object back to this one. 
# In this case, it's specifying that each Category object should have a related manager named 'items' that can be used to retrieve all related Item objects. Finally, on_delete specifies what should happen when the related object is deleted. In this case, it's set to models.CASCADE,
# which means that when a Category object is deleted, all related Item objects will also be deleted.