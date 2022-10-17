from tkinter.tix import WINDOW
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# Create your views here.
def get_home(request):
    return HttpResponse("<h1>Hello, Welcome to my website!</h1>")


def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product": {
            "name": product.name,
            "description": product.description,
            "price": product.price,
        }
    }
    return render(request, "product-detail.html", context)


def get_products(request):
    products = Product.objects.all()
    new_products = []
    for product in products:
        new_products.append({"name": product.name, "price": product.price})

    context = {"products": new_products}

    return render(request, "product-list.html", context)
