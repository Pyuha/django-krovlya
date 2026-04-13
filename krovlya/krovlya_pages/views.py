from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Category, Manufacturer, Product


def main(request):
    """Главная страница"""
    return render(request, "main.html")


def contacts(request):
    """Страница контактов"""
    return render(request, "contacts.html")


def business(request):
    """Страница для бизнеса"""
    return render(request, "for_business.html")


def service(request):
    """Страница услуг"""
    return render(request, "services.html")


def delivery(request):
    """Страница доставки"""
    return render(request, "delivery.html")


def about(request):
    """Страница о компании"""
    return render(request, "about.html")


def product_list(request, category_slug=None):
    """Каталог товаров с фильтрацией и пагинацией"""
    category = None
    categories = Category.objects.filter(parent=None)  # Только корневые
    products = Product.objects.filter(available=True)

    # Фильтр по категории
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        # Включаем товары из подкатегорий
        child_categories = category.children.all()
        if child_categories.exists():
            all_cats = [category] + list(child_categories)
            products = products.filter(category__in=all_cats)
        else:
            products = products.filter(category=category)

    # Фильтр по производителям
    manufacturers = Manufacturer.objects.all()
    selected_manufacturers = request.GET.getlist('manufacturer')
    if selected_manufacturers:
        products = products.filter(manufacturer__slug__in=selected_manufacturers)

    # Фильтр по цене
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    if price_min:
        products = products.filter(price__gte=price_min)
    if price_max:
        products = products.filter(price__lte=price_max)

    # Сортировка
    sort = request.GET.get('sort', 'name')
    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'name':
        products = products.order_by('name')

    # Подкатегории для сайдбара
    subcategories = []
    parent_category = None
    if category:
        if category.children.exists():
            # Это родительская категория — показываем её подкатегории
            subcategories = category.children.all()
            parent_category = category
        elif category.parent:
            # Это подкатегория — показываем подкатегории родителя
            subcategories = category.parent.children.all()
            parent_category = category.parent

    # Пагинация — 21 товар на страницу (7 рядов по 3)
    paginator = Paginator(products, 21)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'categories': categories,
        'subcategories': subcategories,
        'parent_category': parent_category,
        'manufacturers': manufacturers,
        'selected_manufacturers': selected_manufacturers,
        'products': page_obj,
        'page_obj': page_obj,
        'current_sort': sort,
    }
    return render(request, 'catalog.html', context)


def product_detail(request, id, slug):
    """Детальная страница товара"""
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    # Похожие товары (из той же категории)
    related_products = Product.objects.filter(
        category=product.category,
        available=True
    ).exclude(id=product.id)[:4]

    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'product_detail.html', context)