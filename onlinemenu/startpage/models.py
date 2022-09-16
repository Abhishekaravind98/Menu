from enum import Enum
from unicodedata import category
from django.db import models
from django.db.models.deletion import CASCADE



class Category(models.Model):
    class Status(Enum):   
        Active = "Activated"
        Deleted= "Deleted"
        Inactive = "Inactive"
        def __str__(self):
            return self.name
    name = models.CharField(max_length=100)
    images = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modifield_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    #images = models.CharField(max_length=10000000)
    status = models.CharField(max_length=100, choices=[(i.name, i) for i in Status], default=Status.Active)
    
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modifield_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self):
        return self.name


class Dish(models.Model):
    subcat = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    images = models.ImageField(upload_to='images',null=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modifield_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self):
        return self.name