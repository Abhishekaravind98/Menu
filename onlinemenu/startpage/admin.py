from django.contrib import admin
from .models import Category, SubCategory,Dish

# user - admin | pass- password


admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(SubCategory)
