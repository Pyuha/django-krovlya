from django.urls import path
from . import views

app_name = 'krovlya_pages'

urlpatterns = [
    path('', views.main, name='main'),
    path('contacts/', views.contacts, name='contacts'),
    path('for-business/', views.business, name='business'),
    path('services/', views.service, name='service'),
    path('delivery/', views.delivery, name='delivery'),
    path('about/', views.about, name='about'),
    path('catalog/', views.product_list, name='product_list'),
    path('catalog/product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('catalog/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
]