from django.forms import ModelForm
from .models import Category, Dish

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        

class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = '__all__'
        