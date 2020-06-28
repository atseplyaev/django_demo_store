from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, ListView
from .models import Product


class HomePageView(ListView):
    template_name = 'index.html'
    context_object_name = 'products'
    model = Product


class ProductListView(ListView):
    template_name = 'products.html'
    context_object_name = 'products'
    model = Product


class ProductDetailView(DetailView):
    template_name = 'product.html'
    model = Product

