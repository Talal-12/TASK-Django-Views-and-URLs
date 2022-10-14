from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def get_home(request):
    return HttpResponse("<h1>Hello, Welcome to my website!</h1>")


def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    return HttpResponse(
        f"""
                    <div><strong>Product:</strong> {product.name}</div>
                    <div><strong>Price:</strong> {product.price}KD</div>
                    <div><strong>Details:</strong> {product.description}</div>
                    """
    )
