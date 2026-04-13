import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'krovlya.settings')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
django.setup()

from krovlya_pages.models import Category, Manufacturer, Product

# ==========================================
# ОЧИСТКА
# ==========================================
print("Очищаем старые данные...")
Product.objects.all().delete()
Category.objects.all().delete()
Manufacturer.objects.all().delete()
print("Очистка завершена.")

# ==========================================
# КАТЕГОРИИ
# ==========================================
categories = {}

parent_cats = [
    ('Кровля', 'krovlya', 1),
    ('Фасад', 'fasad', 2),
    ('Водосток', 'vodostok', 3),
    ('Ограждения', 'ograzhdeniya', 4),
    ('Утепление', 'uteplenie', 5),
    ('Пиломатериалы', 'pilomaterialy', 6),
    ('Окна', 'okna', 7),
    ('Стройхимия', 'stroyhimiya', 8),
]

for name, slug, order in parent_cats:
    cat = Category.objects.create(name=name, slug=slug, order=order)
    categories[slug] = cat

sub_krovlya = [
    ('Металлочерепица', 'metallocherepitsa', 10),
    ('Профнастил', 'profnastil', 11),
    ('Гибкая черепица', 'gibkaya-cherepitsa', 12),
    ('Композитная черепица', 'kompozitnaya-cherepitsa', 13),
    ('Фальцевая кровля', 'faltsevaya-krovlya', 14),
]

for name, slug, order in sub_krovlya:
    cat = Category.objects.create(name=name, slug=slug, order=order, parent=categories['krovlya'])
    categories[slug] = cat

sub_fasad = [
    ('Сайдинг', 'sayding', 20),
    ('Фасадные панели', 'fasadnye-paneli', 21),
    ('Планкен', 'planken', 22),
]

for name, slug, order in sub_fasad:
    cat = Category.objects.create(name=name, slug=slug, order=order, parent=categories['fasad'])
    categories[slug] = cat

sub_uteplenie = [
    ('Минеральная вата', 'mineralnaya-vata', 30),
    ('Экструдированный пенополистирол', 'xps', 31),
    ('PIR-плиты', 'pir-plity', 32),
]

for name, slug, order in sub_uteplenie:
    cat = Category.objects.create(name=name, slug=slug, order=order, parent=categories['uteplenie'])
    categories[slug] = cat

print(f"Категорий создано: {Category.objects.count()}")

# ==========================================
# ПРОИЗВОДИТЕЛИ
# ==========================================
manufacturers = {}

mfr_list = [
    ('Grand Line', 'grand-line', 'Россия'),
    ('Технониколь', 'tehnonikol', 'Россия'),
    ('Metal Profile', 'metal-profile', 'Россия'),
    ('Docke', 'docke', 'Германия'),
    ('AquaSystem', 'aquasystem', 'Россия'),
    ('Rockwool', 'rockwool', 'Дания'),
    ('Пеноплэкс', 'penoplex', 'Россия'),
    ('Velux', 'velux', 'Дания'),
    ('Fakro', 'fakro', 'Польша'),
    ('Ceresit', 'ceresit', 'Германия'),
    ('Paroc', 'paroc', 'Финляндия'),
    ('Ruukki', 'ruukki', 'Финляндия'),
]

for name, slug, country in mfr_list:
    mfr = Manufacturer.objects.create(name=name, slug=slug, country=country)
    manufacturers[slug] = mfr

print(f"Производителей создано: {Manufacturer.objects.count()}")

# ==========================================
# ТОВАРЫ
# ==========================================

# --- МЕТАЛЛОЧЕРЕПИЦА ---

Product.objects.create(
    name='Металлочерепица "Квинта плюс" 0,5 Satin RAL 8017 шоколад',
    slug='metallocherepitsa-kvinta-plus-satin-ral-8017',
    category=categories['metallocherepitsa'],
    manufacturer=manufacturers['grand-line'],
    short_description='Оригинальный рисунок профиля металлочерепицы Kvinta plus.',
    description='Металлочерепица Kvinta plus изготовлена из оцинкованной стали, устойчивой к значительным механическим нагрузкам.',
    price=850,
    price_unit='м²',
    available=True,
    stock=500,
    brand='Grand Line',
    material='оцинкованная сталь',
    color='RAL 8017',
    color_name='шоколад',
    coating='Satin',
    coating_thickness='25 мкм',
    thickness='0,5 мм',
    country_brand='Россия',
    country_production='Россия',
    purpose='для кровли',
    length='0,47 - 8,00 м',
    width_total='1210 мм',
    width_working='1150 мм',
    wave_height='20 мм',
    step_height='30 мм',
    step_pitch='350 мм',
    roof_angle='от 12°',
    profile_type='Металлочерепица',
    form_type='Kvinta plus',
    surface_gloss='глянцевая',
    surface_texture='гладкая',
    back_side='эпоксидная серая',
    protective_layer='Zn 100-140 г/м²',
    warranty_appearance='10 лет',
    warranty_technical='20 лет',
    resistance='к УФ/UV3',
)
print("  + Квинта плюс")

Product.objects.create(
    name='Металлочерепица "Монтеррей" 0,5 Satin RAL 3005 красное вино',
    slug='metallocherepitsa-monterrey-satin-ral-3005',
    category=categories['metallocherepitsa'],
    manufacturer=manufacturers['grand-line'],
    short_description='Классический профиль металлочерепицы, повторяющий рисунок натуральной черепицы.',
    description='Самый популярный профиль металлочерепицы в России.',
    price=780,
    old_price=920,
    price_unit='м²',
    available=True,
    stock=350,
    brand='Grand Line',
    material='оцинкованная сталь',
    color='RAL 3005',
    color_name='красное вино',
    coating='Satin',
    coating_thickness='25 мкм',
    thickness='0,5 мм',
    country_brand='Россия',
    country_production='Россия',
    purpose='для кровли',
    length='0,47 - 8,00 м',
    width_total='1180 мм',
    width_working='1100 мм',
    wave_height='25 мм',
    step_height='15 мм',
    step_pitch='350 мм',
    roof_angle='от 14°',
    profile_type='Металлочерепица',
    form_type='Монтеррей',
    surface_gloss='глянцевая',
    surface_texture='гладкая',
    back_side='эпоксидная серая',
    protective_layer='Zn 100-140 г/м²',
    warranty_appearance='10 лет',
    warranty_technical='20 лет',
    resistance='к УФ/UV3',
)
print("  + Монтеррей")

Product.objects.create(
    name='Металлочерепица "Камея" 0,45 PE RAL 9003 белый',
    slug='metallocherepitsa-kameya-pe-ral-9003',
    category=categories['metallocherepitsa'],
    manufacturer=manufacturers['metal-profile'],
    short_description='Элегантный профиль с плавными линиями и выраженным рельефом.',
    price=690,
    price_unit='м²',
    available=True,
    stock=180,
    brand='Metal Profile',
    material='оцинкованная сталь',
    color='RAL 9003',
    color_name='сигнально-белый',
    coating='PE (полиэстер)',
    coating_thickness='25 мкм',
    thickness='0,45 мм',
    country_brand='Россия',
    country_production='Россия',
    purpose='для кровли',
    width_total='1220 мм',
    width_working='1140 мм',
    wave_height='30 мм',
    profile_type='Металлочерепица',
    form_type='Камея',
    surface_gloss='глянцевая',
    surface_texture='гладкая',
    warranty_appearance='5 лет',
    warranty_technical='10 лет',
)
print("  + Камея")

Product.objects.create(
    name='Металлочерепица "Классик" 0,5 Velur RAL 7024 серый',
    slug='metallocherepitsa-klassik-velur-ral-7024',
    category=categories['metallocherepitsa'],
    manufacturer=manufacturers['grand-line'],
    short_description='Металлочерепица с бархатистым покрытием Velur. Премиальный вид и долговечность.',
    price=1150,
    price_unit='м²',
    available=True,
    stock=120,
    brand='Grand Line',
    material='оцинкованная сталь',
    color='RAL 7024',
    color_name='графитовый серый',
    coating='Velur',
    coating_thickness='35 мкм',
    thickness='0,5 мм',
    country_brand='Россия',
    country_production='Россия',
    purpose='для кровли',
    width_total='1180 мм',
    width_working='1100 мм',
    profile_type='Металлочерепица',
    form_type='Классик',
    surface_gloss='матовая',
    surface_texture='бархатистая',
    warranty_appearance='15 лет',
    warranty_technical='30 лет',
    resistance='к УФ/UV4',
)
print("  + Классик Velur")

# --- ПРОФНАСТИЛ ---

Product.objects.create(
    name='Профнастил С-8 0,5 Satin RAL 6005 зелёный мох',
    slug='profnastil-s8-satin-ral-6005',
    category=categories['profnastil'],
    manufacturer=manufacturers['grand-line'],
    short_description='Стеновой профнастил с минимальной высотой волны.',
    price=520,
    price_unit='лист',
    available=True,
    stock=200,
    brand='Grand Line',
    material='оцинкованная сталь',
    color='RAL 6005',
    color_name='зелёный мох',
    coating='Satin',
    coating_thickness='25 мкм',
    thickness='0,5 мм',
    country_brand='Россия',
    country_production='Россия',
    purpose='для стен и заборов',
    length='0,5 - 12,0 м',
    width_total='1200 мм',
    width_working='1150 мм',
    wave_height='8 мм',
    profile_type='Профнастил',
    form_type='С-8',
    surface_gloss='глянцевая',
    surface_texture='гладкая',
    warranty_appearance='10 лет',
    warranty_technical='20 лет',
)
print("  + Профнастил С-8")

Product.objects.create(
    name='Профнастил С-21 0,5 Satin RAL 8017 шоколад',
    slug='profnastil-s21-satin-ral-8017',
    category=categories['profnastil'],
    manufacturer=manufacturers['grand-line'],
    short_description='Универсальный профнастил с высотой волны 21 мм.',
    price=640,
    price_unit='лист',
    available=True,
    stock=300,
    brand='Grand Line',
    material='оцинкованная сталь',
    color='RAL 8017',
    color_name='шоколад',
    coating='Satin',
    thickness='0,5 мм',
    purpose='универсальный',
    width_total='1051 мм',
    width_working='1000 мм',
    wave_height='21 мм',
    profile_type='Профнастил',
    form_type='С-21',
    surface_gloss='глянцевая',
    warranty_appearance='10 лет',
    warranty_technical='20 лет',
)
print("  + Профнастил С-21")

Product.objects.create(
    name='Профнастил НС-35 0,7 PE RAL 5005 синий',
    slug='profnastil-ns35-pe-ral-5005',
    category=categories['profnastil'],
    manufacturer=manufacturers['metal-profile'],
    short_description='Несуще-стеновой профнастил повышенной жёсткости.',
    price=890,
    price_unit='лист',
    available=True,
    stock=150,
    brand='Metal Profile',
    material='оцинкованная сталь',
    color='RAL 5005',
    color_name='сигнально-синий',
    coating='PE (полиэстер)',
    thickness='0,7 мм',
    purpose='для кровли и несущих конструкций',
    width_total='1060 мм',
    width_working='1000 мм',
    wave_height='35 мм',
    profile_type='Профнастил',
    form_type='НС-35',
    warranty_appearance='5 лет',
    warranty_technical='15 лет',
)
print("  + Профнастил НС-35")

# --- ГИБКАЯ ЧЕРЕПИЦА ---

Product.objects.create(
    name='Гибкая черепица SHINGLAS "Ранчо" коричневый',
    slug='gibkaya-cherepitsa-shinglas-rancho-korichnevyj',
    category=categories['gibkaya-cherepitsa'],
    manufacturer=manufacturers['tehnonikol'],
    short_description='Однослойная гибкая черепица. Простой и надёжный материал для скатных кровель.',
    description='Серия Ранчо — экономичное решение с гарантией от Технониколь.',
    price=450,
    price_unit='м²',
    available=True,
    stock=600,
    brand='SHINGLAS',
    material='стеклохолст, битум, базальтовый гранулят',
    color_name='коричневый',
    country_brand='Россия',
    country_production='Россия',
    purpose='для скатных кровель',
    profile_type='Гибкая черепица',
    form_type='Ранчо',
    warranty_appearance='15 лет',
    warranty_technical='20 лет',
)
print("  + SHINGLAS Ранчо")

Product.objects.create(
    name='Гибкая черепица SHINGLAS "Джаз" серый гранит',
    slug='gibkaya-cherepitsa-shinglas-jazz-seryj-granit',
    category=categories['gibkaya-cherepitsa'],
    manufacturer=manufacturers['tehnonikol'],
    short_description='Двухслойная гибкая черепица с объёмным рисунком.',
    price=890,
    old_price=1050,
    price_unit='м²',
    available=True,
    stock=250,
    brand='SHINGLAS',
    material='стеклохолст, битум, базальтовый гранулят',
    color_name='серый гранит',
    country_brand='Россия',
    country_production='Россия',
    purpose='для скатных кровель',
    profile_type='Гибкая черепица',
    form_type='Джаз',
    warranty_appearance='30 лет',
    warranty_technical='50 лет',
)
print("  + SHINGLAS Джаз")

Product.objects.create(
    name='Гибкая черепица SHINGLAS "Кантри" зелёный',
    slug='gibkaya-cherepitsa-shinglas-kantri-zelenyj',
    category=categories['gibkaya-cherepitsa'],
    manufacturer=manufacturers['tehnonikol'],
    short_description='Однослойная черепица с формой нарезки "Кантри".',
    price=380,
    price_unit='м²',
    available=True,
    stock=400,
    brand='SHINGLAS',
    material='стеклохолст, битум, базальтовый гранулят',
    color_name='зелёный',
    country_brand='Россия',
    purpose='для скатных кровель',
    profile_type='Гибкая черепица',
    form_type='Кантри',
    warranty_appearance='15 лет',
    warranty_technical='20 лет',
)
print("  + SHINGLAS Кантри")

# --- КОМПОЗИТНАЯ ЧЕРЕПИЦА ---

Product.objects.create(
    name='Композитная черепица Ruukki Finnera коричневый',
    slug='kompozitnaya-cherepitsa-ruukki-finnera-korichnevyj',
    category=categories['kompozitnaya-cherepitsa'],
    manufacturer=manufacturers['ruukki'],
    short_description='Модульная композитная черепица с каменной посыпкой.',
    price=1850,
    price_unit='м²',
    available=True,
    stock=80,
    brand='Ruukki',
    material='сталь с каменной посыпкой',
    color_name='коричневый',
    country_brand='Финляндия',
    country_production='Финляндия',
    purpose='для кровли',
    profile_type='Композитная черепица',
    form_type='Finnera',
    surface_texture='каменная посыпка',
    warranty_appearance='30 лет',
    warranty_technical='50 лет',
)
print("  + Ruukki Finnera")

# --- ФАЛЬЦЕВАЯ КРОВЛЯ ---

Product.objects.create(
    name='Фальцевая кровля Кликфальц 0,5 Satin RAL 7024 серый',
    slug='faltsevaya-krovlya-klikfalts-satin-ral-7024',
    category=categories['faltsevaya-krovlya'],
    manufacturer=manufacturers['grand-line'],
    short_description='Самозащёлкивающийся фальц для быстрого монтажа.',
    price=980,
    price_unit='м²',
    available=True,
    stock=150,
    brand='Grand Line',
    material='оцинкованная сталь',
    color='RAL 7024',
    color_name='графитовый серый',
    coating='Satin',
    thickness='0,5 мм',
    country_brand='Россия',
    purpose='для кровли',
    width_working='340 мм',
    profile_type='Фальцевая кровля',
    form_type='Кликфальц',
    warranty_appearance='10 лет',
    warranty_technical='20 лет',
)
print("  + Кликфальц")

# --- САЙДИНГ ---

Product.objects.create(
    name='Сайдинг виниловый D4.5 Docke Premium пломбир',
    slug='sayding-vinilovyj-docke-premium-plombir',
    category=categories['sayding'],
    manufacturer=manufacturers['docke'],
    short_description='Виниловый сайдинг премиум-класса. Не выгорает, не трескается.',
    price=320,
    price_unit='шт.',
    available=True,
    stock=1000,
    brand='Docke',
    material='ПВХ',
    color_name='пломбир',
    country_brand='Германия',
    country_production='Россия',
    purpose='для фасада',
    length='3660 мм',
    width_total='240 мм',
    profile_type='Сайдинг',
    form_type='D4.5',
    warranty_appearance='25 лет',
)
print("  + Сайдинг D4.5 пломбир")

Product.objects.create(
    name='Сайдинг виниловый Blockhouse Docke слива',
    slug='sayding-vinilovyj-blockhouse-docke-sliva',
    category=categories['sayding'],
    manufacturer=manufacturers['docke'],
    short_description='Сайдинг под бревно. Имитация натурального дерева.',
    price=380,
    price_unit='шт.',
    available=True,
    stock=500,
    brand='Docke',
    material='ПВХ',
    color_name='слива',
    country_brand='Германия',
    purpose='для фасада',
    profile_type='Сайдинг',
    form_type='Blockhouse',
    warranty_appearance='25 лет',
)
print("  + Сайдинг Blockhouse слива")

# --- ФАСАДНЫЕ ПАНЕЛИ ---

Product.objects.create(
    name='Фасадная панель Docke Stein тёмный орех',
    slug='fasadnaya-panel-docke-stein-temnyj-oreh',
    category=categories['fasadnye-paneli'],
    manufacturer=manufacturers['docke'],
    short_description='Фасадная панель с имитацией камня. Коллекция Stein.',
    price=650,
    price_unit='шт.',
    available=True,
    stock=300,
    brand='Docke',
    material='полипропилен',
    color_name='тёмный орех',
    country_brand='Германия',
    purpose='для цоколя и фасада',
    length='1098 мм',
    width_total='400 мм',
    profile_type='Фасадная панель',
    form_type='Stein',
)
print("  + Фасадная панель Stein")

# --- ВОДОСТОК ---

Product.objects.create(
    name='Водосточная система Grand Line 125/90 RAL 8017 шоколад (желоб 3м)',
    slug='vodostochnaya-sistema-grand-line-125-90-ral-8017-zhelob',
    category=categories['vodostok'],
    manufacturer=manufacturers['grand-line'],
    short_description='Металлический водосточный желоб 3 метра. Система 125/90.',
    price=720,
    price_unit='шт.',
    available=True,
    stock=200,
    brand='Grand Line',
    material='оцинкованная сталь с полимерным покрытием',
    color='RAL 8017',
    color_name='шоколад',
    country_brand='Россия',
    purpose='для водоотведения',
    length='3000 мм',
    profile_type='Водосточная система',
)
print("  + Желоб 3м")

Product.objects.create(
    name='Водосточная труба Grand Line 125/90 RAL 8017 шоколад (3м)',
    slug='vodostochnaya-truba-grand-line-125-90-ral-8017',
    category=categories['vodostok'],
    manufacturer=manufacturers['grand-line'],
    short_description='Водосточная труба 3 метра. Диаметр 90 мм.',
    price=680,
    price_unit='шт.',
    available=True,
    stock=180,
    brand='Grand Line',
    material='оцинкованная сталь с полимерным покрытием',
    color='RAL 8017',
    color_name='шоколад',
    country_brand='Россия',
    purpose='для водоотведения',
    length='3000 мм',
    profile_type='Водосточная система',
)
print("  + Труба 3м")

# ==========================================
# ИТОГ
# ==========================================
print("")
print("=" * 50)
print(f"Категорий:      {Category.objects.count()}")
print(f"Производителей: {Manufacturer.objects.count()}")
print(f"Товаров:        {Product.objects.count()}")
print("=" * 50)
print("Импорт завершён успешно!")