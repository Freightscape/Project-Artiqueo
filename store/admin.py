from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'slug', 'price', 'in-stock', 'created', 'updated']
    list_filter = ['in-stock', 'is-active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}