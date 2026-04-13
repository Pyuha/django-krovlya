from django.urls import path
from . import views

app_name = 'krovlya_pages'

urlpatterns = [
    path('', views.main, name='main'),
    path('contacts/', views.contacts, name='contacts'),
    path('business/', views.business, name='business'),
    path('service/', views.service, name='service'),
    path('delivery/', views.delivery, name='delivery'),
    path('catalog/', views.product_list, name='product_list'),
    path('catalog/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('catalog/product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]