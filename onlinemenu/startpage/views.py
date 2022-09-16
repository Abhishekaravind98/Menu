
from django.shortcuts import render
from django.http import HttpResponse
from .serialzers import CategorySerializer,SubCategorySerializer, DishSerializer
from rest_framework.response import Response
from .models import Category, SubCategory, Dish
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import F


class WebResponse(dict):
    def __init__(self, status=200, message='success', data=None):
        dict.__init__(self, status=status, message=message, data=data)

class CategoryList(APIView):

    def get(self, request, format=None):
        category = Category.objects.all().values()
        # return Response(WebResponse(status=404, data=categories), status=status.HTTP_200_OK)
        return Response(WebResponse( data=category))

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):

    def get(self, request, pk):
        category = Category.objects.filter(pk=pk).values()
        return Response(WebResponse( data=category))

    def put(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if (serializer.is_valid(raise_exception=True)):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        Category.objects.filter(pk=pk).update(status=False)
        return Response({"message": "record deleted"}, status=200)


class DishList(APIView):
    def get(self, request, format=None):
        dish = Dish.objects.all().values()
        # return Response(WebResponse(status=404, data=categories), status=status.HTTP_200_OK)
        return Response(WebResponse( data=dish))

    def post(self, request):
        serializer = DishSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DishDetail(APIView):

    def get(self, request, pk):
        dish = Dish.objects.filter(pk=pk).values().annotate(category_name=F('category__name'))
        return Response(WebResponse( data=dish))

    def put(self, request, pk):
        dish = Dish.objects.get(pk=pk)
        serializer = DishSerializer(dish, data=request.data)
        if (serializer.is_valid(raise_exception=True)):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        Dish.objects.filter(pk=pk).update(status=False)
        return Response({"message": "record deleted"}, status=200)



class SubCategoryList(APIView):

    def get(self, request, format=None):
        subcategory = SubCategory.objects.all().values()
        # return Response(WebResponse(status=404, data=categories), status=status.HTTP_200_OK)
        return Response(WebResponse( data=subcategory))

    def post(self, request):
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubCategoryDetail(APIView):

    def get(self, request, pk):
        subcategory = SubCategory.objects.filter(pk=pk).values()
        return Response(WebResponse( data=subcategory))

    def put(self, request, pk):
        category = SubCategory.objects.get(pk=pk)
        serializer = SubCategorySerializer(category, data=request.data)
        if (serializer.is_valid(raise_exception=True)):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        SubCategory.objects.filter(pk=pk).update(status=False)
        return Response({"message": "record deleted"}, status=200)





def home(request):
    category = Category.objects.all()
    subcat= SubCategory.objects.all()
    
    subcategoryid = request.GET.get('category')
    if subcategoryid:
        food= Dish.objects.filter(subcategory= subcategoryid)
        
    else:
        food=Dish.objects.all()
    
    context= {'category':category,'subcat':subcat,'foods':food}
    return render(request,'startpage/home.html', context)

