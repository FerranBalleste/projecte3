from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  price = models.DecimalField(max_digits=6, decimal_places=2)
  #image = models.ImageField(upload_to='products/', blank=True)

  def __str__(self):
    return self.title

class Cart(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  payment = models.BooleanField(default=False)

  def __str__(self):
    return f"{self.user.username}'s Cart"

class CartItem(models.Model):
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=1)

  def get_total(self):
    return self.quantity * self.product.price

  def __str__(self):
    return f"{self.product.title} ({self.quantity})"