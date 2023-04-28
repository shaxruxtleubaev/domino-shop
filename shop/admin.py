from django.contrib.admin import *
from .models import (
	Product, Category, Color,
	Size, Country, Brand
)


@register(Product)
class ProductAdmin(ModelAdmin):
	list_display = ('id', 'product_name', 'price', 'stock', 'date')
	list_display_links = ('id', 'product_name')
	ordering = ('id', )


@register(Category)
class CategoryAdmin(ModelAdmin):
	list_display = ('id', 'category_name')
	list_display_links = ('id', 'category_name')
	prepopulated_fields = {'slug': ('category_name',)}
	ordering = ('id', )


'''--------------------------------------------------'''


@register(Color)
class ColorAdmin(ModelAdmin):
	list_display = ('id', 'color_name')
	list_display_links = ('id', 'color_name')
	ordering = ('id',)

@register(Size)
class SizeAdmin(ModelAdmin):
	list_display = ('id', 'size_name')
	list_display_links = ('id', 'size_name')
	ordering = ('id',)

@register(Country)
class CountryAdmin(ModelAdmin):
	list_display = ('id', 'country_name')
	list_display_links = ('id', 'country_name')
	ordering = ('id',)

@register(Brand)
class BrandAdmin(ModelAdmin):
	list_display = ('id', 'brand_name')
	list_display_links = ('id', 'brand_name')
	ordering = ('id',)
