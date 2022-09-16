from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('api/category', views.CategoryList.as_view()),
    path('api/category/<int:pk>',views.CategoryDetail.as_view()),
    path('api/dish',views.DishList.as_view()),
    path('api/dish/<int:pk>',views.DishDetail.as_view()),
    path('api/subcategory',views.SubCategoryList.as_view()),
    path('api/subcategory/<int:pk>',views.SubCategoryDetail.as_view()),
]