from django.db import models
from django.contrib.auth.models import User
from enum import Enum


class ProductCategory(Enum):
  TECHNOLOGY = "Technology"
  FOOD = "Food"
  CLOTHING = "Clothing"


class Product(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  price = models.DecimalField(max_digits=6, decimal_places=2)
  category = models.CharField(max_length=20, choices=[(category.name, category.value) for category in ProductCategory])
  #image = models.ImageField(upload_to='products/', blank=True)

  def __str__(self):
    return self.title


class Cart(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  direction = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  payment = models.BooleanField(default=False)

  def get_total(self):
    cart_items = CartItem.objects.filter(cart=self)
    return sum(item.get_total() for item in cart_items)

  def pay(self):
    self.payment = True
    self.save()

  def __str__(self):
    return f"{self.user.username}'s Cart"


class CartItem(models.Model):
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=1)
  price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)
  
  def get_total(self):
    return self.quantity * self.price_at_purchase
  
  # On creation, save price
  def save(self, *args, **kwargs):
    if not self.pk:
      self.price_at_purchase = self.product.price
    super().save(*args, **kwargs)

  def __str__(self):
    return f"{self.product.title} ({self.quantity})"
  

class Review(models.Model):
    rating = models.IntegerField()
    description = models.TextField()
    product = models.ForeignKey(Product, related_name="ratingproduct", on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.rating} ({self.user})"