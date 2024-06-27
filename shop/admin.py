from django.contrib import admin
from  .models import *

class ReviewInline(admin.TabularInline):
    model = Review
    fields = ["rating", "product", "user"]
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]
    search_fields = ["name", "description"]

class CartItemInline(admin.TabularInline):
    model = CartItem
    fields = ["product", "quantity"]
    ordering = ("product",)

class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
    search_fields = ["user","created_at"]

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
