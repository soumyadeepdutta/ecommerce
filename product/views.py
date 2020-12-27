from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


class ProductList(ListView):
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'product_list'


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/details.html'
    context_object_name = 'product'
