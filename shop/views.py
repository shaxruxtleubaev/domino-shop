from django.shortcuts import render
from .models import(
     Product, Category,
     Color, Size, Country, Brand
)
from django.shortcuts import get_list_or_404

from datetime import datetime


'''--------------------------------------------------'''


def index(request):
     trend = get_list_or_404(
          Product,
          trend=True
     )

     #---

     year = datetime.now().strftime('%Y')
     month = datetime.now().strftime('%m')

     new = Product.objects.filter(
          date__year=year,
          date__month=month
     )

     #---

     categories = Category.objects.all()

     return render(
          request, 'index.html',
          {
               'trend': trend,
               'new': new,
               'categories': categories
          }
     )


'''--------------------------------------------------'''


def product_list(request):
     return render(
          request, 'shop/product_list.html',
          {
               'products': Product.objects.all()
          }
     )

def product_detail(request, pk):
     return render(
          request, 'shop/product_detail.html',
          {
               'product': Product.objects.get(id=pk)
          }
     )


'''--------------------------------------------------'''


def contacts(request):
     return render(
          request, 'contact.html'
     )

def liked(request):
     return render(
          request, 'liked.html'
     )


'''--------------------------------------------------'''


def category(request, category_slug):
     products = get_list_or_404(
          Product,
          category__slug=category_slug
     )

     return render(
          request, 'shop/category.html',
          {
               'products': products
          }
     )

