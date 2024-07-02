from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
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

def login_view(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user:
      login(request, user)
      return render('home')  # Redirect to your home view
    else:
      # Return Invalid
      pass
  else:
    # Display login form
    return render(request, 'login.html')