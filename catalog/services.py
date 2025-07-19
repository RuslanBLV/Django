from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_product_from_cache():
    """Получает данные по продуктам из кеша, если кеш пуст, берет из бд."""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'product_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_products_by_category(category_name):
    """Возвращает QuerySet продуктов, относящихся к категории с заданным именем."""
    return Product.objects.filter(category_product__name=category_name, unpublish=True)
