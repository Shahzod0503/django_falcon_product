from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.ecommerrs.views import CategoryModelViews, ProductModelViews

router = DefaultRouter()
router.register('category', CategoryModelViews, 'category')
router.register('product', ProductModelViews, 'product')
urlpatterns = [
    path('', include(router.urls))
]
