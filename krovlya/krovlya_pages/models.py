from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        null=True, blank=True, related_name='children'
    )
    image = models.ImageField(
        'Изображение категории',
        upload_to='categories/',
        blank=True, null=True
    )
    order = models.PositiveIntegerField('Порядок сортировки', default=0)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['order', 'name']

    def get_absolute_url(self):
        return reverse('krovlya_pages:product_list_by_category', args=[self.slug])

    def __str__(self):
        full_path = [self.name]
        parent = self.parent
        while parent is not None:
            full_path.append(parent.name)
            parent = parent.parent
        return ' → '.join(full_path[::-1])


class Manufacturer(models.Model):
    name = models.CharField('Название', max_length=200)
    slug = models.SlugField('URL', max_length=200, unique=True)
    logo = models.ImageField('Логотип', upload_to='manufacturers/', blank=True)
    country = models.CharField('Страна бренда', max_length=100, blank=True)
    description = models.TextField('Описание', blank=True)

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('Название', max_length=500)
    slug = models.SlugField('URL', max_length=500, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='products', verbose_name='Категория'
    )
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='products', verbose_name='Производитель'
    )
    short_description = models.TextField('Краткое описание', blank=True)
    description = models.TextField('Полное описание', blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    old_price = models.DecimalField(
        'Старая цена', max_digits=10, decimal_places=2,
        null=True, blank=True, help_text='Для отображения скидки'
    )
    price_unit = models.CharField(
        'Единица измерения', max_length=50,
        default='шт.', help_text='шт., м², м.п., лист и т.д.'
    )
    available = models.BooleanField('В наличии', default=True)
    stock = models.PositiveIntegerField('Остаток на складе', default=0)
    image = models.ImageField('Главное фото', upload_to='products/', blank=True)

    brand = models.CharField('Бренд', max_length=200, blank=True)
    material = models.CharField('Материал', max_length=200, blank=True)
    color = models.CharField('Цвет (RAL)', max_length=100, blank=True)
    color_name = models.CharField('Цветовой оттенок', max_length=200, blank=True)
    coating = models.CharField('Покрытие', max_length=200, blank=True)
    coating_thickness = models.CharField('Толщина покрытия', max_length=100, blank=True)
    thickness = models.CharField('Толщина', max_length=100, blank=True)
    country_brand = models.CharField('Страна бренда', max_length=100, blank=True)
    country_production = models.CharField('Страна производства', max_length=100, blank=True)
    purpose = models.CharField('Назначение', max_length=200, blank=True)

    length = models.CharField('Длина изделия', max_length=100, blank=True)
    width_total = models.CharField('Ширина общая', max_length=100, blank=True)
    width_working = models.CharField('Ширина рабочая', max_length=100, blank=True)

    wave_height = models.CharField('Высота волны', max_length=100, blank=True)
    step_height = models.CharField('Высота ступеньки', max_length=100, blank=True)
    step_pitch = models.CharField('Шаг ступеньки', max_length=100, blank=True)
    roof_angle = models.CharField('Угол наклона кровли', max_length=100, blank=True)
    profile_type = models.CharField('Вид профиля кровельного материала', max_length=200, blank=True)
    form_type = models.CharField('Тип формы', max_length=200, blank=True)

    surface_gloss = models.CharField('Блеск поверхности', max_length=100, blank=True)
    surface_texture = models.CharField('Текстура поверхности', max_length=100, blank=True)
    back_side = models.CharField('Обратная сторона', max_length=200, blank=True)
    protective_layer = models.CharField('Защитный слой', max_length=200, blank=True)

    warranty_appearance = models.CharField('Гарантия на внешний вид', max_length=100, blank=True)
    warranty_technical = models.CharField('Гарантия на технические характеристики', max_length=100, blank=True)
    resistance = models.CharField('Стойкость', max_length=200, blank=True)

    created = models.DateTimeField('Создан', auto_now_add=True)
    updated = models.DateTimeField('Обновлён', auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('krovlya_pages:product_detail', args=[self.id, self.slug])

    @property
    def has_discount(self):
        return self.old_price and self.old_price > self.price

    @property
    def discount_percent(self):
        if self.has_discount:
            return int(100 - (self.price / self.old_price * 100))
        return 0

    def get_specs(self):
        specs = [
            ('Бренд', self.brand),
            ('Блеск поверхности', self.surface_gloss),
            ('Вид профиля кровельного материала', self.profile_type),
            ('Высота волны', self.wave_height),
            ('Высота ступеньки', self.step_height),
            ('Гарантия на внешний вид', self.warranty_appearance),
            ('Гарантия на технические характеристики', self.warranty_technical),
            ('Длина изделия', self.length),
            ('Защитный слой', self.protective_layer),
            ('Материал', self.material),
            ('Назначение', self.purpose),
            ('Обратная сторона', self.back_side),
            ('Стойкость', self.resistance),
            ('Страна бренда', self.country_brand),
            ('Страна производства', self.country_production),
            ('Текстура поверхности', self.surface_texture),
            ('Тип формы', self.form_type),
            ('Толщина покрытия', self.coating_thickness),
            ('Угол наклона кровли', self.roof_angle),
            ('Цветовой оттенок', self.color_name),
            ('Шаг ступеньки', self.step_pitch),
            ('Ширина общая', self.width_total),
            ('Ширина рабочая', self.width_working),
            ('Цвет', self.color),
            ('Покрытие', self.coating),
            ('Толщина', self.thickness),
        ]
        return [(name, value) for name, value in specs if value]


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='images', verbose_name='Товар'
    )
    image = models.ImageField('Фото', upload_to='products/gallery/')
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фото товаров'
        ordering = ['order']

    def __str__(self):
        return f'Фото {self.order} — {self.product.name}'