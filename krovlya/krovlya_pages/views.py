from django.shortcuts import render

def main(request):
    return render(request, "main.html")

def contacts(request):
    return render(request, "contacts.html")

def business(request):
    return render(request, "for_business.html")

def service(request):
    return render(request, "services.html")

def delivery(request):
    return render(request, "delivery.html")

from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    # Фильтр по категории (через URL)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # Фильтр по цене (через GET-параметры)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    # Фильтр по наличию на складе
    in_stock = request.GET.get('in_stock')
    if in_stock:
        products = products.filter(stock__gt=0)

    # Сортировка
    sort = request.GET.get('sort', 'name')
    if sort in ['name', '-name', 'price', '-price', '-created']:
        products = products.order_by(sort)

    # Поиск по названию
    search = request.GET.get('search', '')
    if search:
        products = products.filter(name__icontains=search)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'min_price': min_price or '',
        'max_price': max_price or '',
        'in_stock': in_stock or '',
        'current_sort': sort,
        'search': search,
    }
    return render(request, 'catalog.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'product_detail.html', {'product': product})
