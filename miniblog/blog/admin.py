from django.contrib import admin
from .models import Post,Contact

# Register your models here.
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']

# admin.site.register(Post)

@admin.register(Contact)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'address', 'message']