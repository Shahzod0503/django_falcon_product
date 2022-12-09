from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from rest_framework.viewsets import ModelViewSet

from apps.ecommerrs.models import Category, Product
from apps.ecommerrs.serializer import CategorySerializer, ProductSerializer


class CategoryModelViews(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class ProductModelViews(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
