from django.contrib import admin
from .models import Customer,Orderedplace,Cart,User,Product
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'name', 'locality', 'city', 'zipcode','state']

@admin.register(Orderedplace)
class OrderedplaceAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product', 'quantity', 'ordered_date', 'status']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'product','quantity']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'selling_price','discounted_price','description','brand','category','product_image']

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['id', 'username', 'password','first_name']