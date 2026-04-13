from django.contrib import admin
from .models import Category, Product, ProductImage, Manufacturer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'parent', 'order']
    list_editable = ['slug', 'order']
    list_filter = ['parent']
    prepopulated_fields = {'slug': ('name',)}


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'manufacturer', 'price', 'available', 'created']
    list_filter = ['available', 'category', 'manufacturer', 'created']
    list_editable = ['price', 'available']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]
    fieldsets = (
        ('Основное', {
            'fields': ('name', 'slug', 'category', 'manufacturer', 'image')
        }),
        ('Описание', {
            'fields': ('short_description', 'description')
        }),
        ('Цена и наличие', {
            'fields': ('price', 'old_price', 'price_unit', 'available', 'stock')
        }),
        ('Характеристики', {
            'classes': ('collapse',),
            'fields': (
                'brand', 'material', 'color', 'color_name', 'coating',
                'coating_thickness', 'thickness', 'country_brand',
                'country_production', 'purpose',
            )
        }),
        ('Размеры', {
            'classes': ('collapse',),
            'fields': ('length', 'width_total', 'width_working')
        }),
        ('Кровля', {
            'classes': ('collapse',),
            'fields': (
                'wave_height', 'step_height', 'step_pitch', 'roof_angle',
                'profile_type', 'form_type',
            )
        }),
        ('Поверхность', {
            'classes': ('collapse',),
            'fields': (
                'surface_gloss', 'surface_texture', 'back_side', 'protective_layer',
            )
        }),
        ('Гарантии', {
            'classes': ('collapse',),
            'fields': ('warranty_appearance', 'warranty_technical', 'resistance')
        }),
    )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'country']
    prepopulated_fields = {'slug': ('name',)}