from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class Home(TemplateView):
    template_name='index.html'

class About(TemplateView):
    template_name='about.html'

class Contact(TemplateView):
    template_name='contact.html'

class Products(TemplateView):
    template_name='products.html'

class Single_Product(TemplateView):
    template_name='single-product.html'