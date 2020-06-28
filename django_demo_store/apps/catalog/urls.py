from django.conf.urls import url, include
from django.urls import path
from .views import HomePageView, ProductListView, ProductDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-item'),
]
