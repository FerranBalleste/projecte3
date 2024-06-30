from django.shortcuts import render, get_object_or_404
from .models import *

def home(request):
  products = Product.objects.all()  # Get all products
  context = {'products': products}
  return render(request, 'home.html', context)

def product_detail(request, product_id):
  product = get_object_or_404(Product, pk=product_id)
  reviews = product.ratingproduct.all().order_by('-created_at')
  context = {'product': product, 'reviews': reviews}
  return render(request, 'product_detail.html', context)

#def index(request):
#    return HttpResponse("Hello, world. You're at the shop index.")