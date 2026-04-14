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


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.filter(parent=None)  # Только корневые
    products = Product.objects.all()
    
    # Для хлебных крошек
    ancestors = []

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        ancestors = category.get_ancestors()
        
        # Получаем товары из текущей категории И всех потомков
        descendant_ids = get_descendant_ids(category)
        products = products.filter(category__id__in=descendant_ids)

    # Производители
    manufacturers = Manufacturer.objects.all()
    selected_manufacturers = request.GET.getlist('manufacturer')
    if selected_manufacturers:
        products = products.filter(manufacturer__slug__in=selected_manufacturers)

    # Собираем полное дерево категорий с информацией об открытых ветках
    category_tree = build_category_tree(categories, category)

    context = {
        'category': category,
        'ancestors': ancestors,
        'category_tree': category_tree,
        'products': products,
        'manufacturers': manufacturers,
        'selected_manufacturers': selected_manufacturers,
    }
    return render(request, 'catalog.html', context)


def get_descendant_ids(category):
    """Рекурсивно получить ID категории и всех потомков"""
    ids = [category.id]
    for child in category.children.all():
        ids.extend(get_descendant_ids(child))
    return ids


def build_category_tree(categories, current_category=None):
    """
    Строит дерево категорий.
    Каждый элемент = {
        'category': Category,
        'children': [...],
        'is_open': bool,      # Раскрыта ли ветка
        'is_active': bool,    # Текущая категория
    }
    """
    # Определяем ID всех предков текущей категории (чтобы раскрыть ветку)
    active_ids = set()
    if current_category:
        active_ids.add(current_category.id)
        parent = current_category.parent
        while parent:
            active_ids.add(parent.id)
            parent = parent.parent

    def _build(cats):
        result = []
        for cat in cats:
            children = cat.children.all()
            is_active = current_category and cat.id == current_category.id
            is_open = cat.id in active_ids
            
            node = {
                'category': cat,
                'children': _build(children) if children.exists() else [],
                'is_open': is_open,
                'is_active': is_active,
                'has_children': children.exists(),
            }
            result.append(node)
        return result

    return _build(categories)