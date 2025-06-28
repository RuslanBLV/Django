from django.db import models


class Category(models.Model):
    """Модель категории для группировки продуктов"""
    name = models.CharField(max_length=200, verbose_name='Категория')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        """Возвращает строковое представление категории — её название"""
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name', ]


class Product(models.Model):
    """Модель продукта, связанного с категорией."""
    name = models.CharField(max_length=150, verbose_name='Продукт')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение', upload_to='media/photos/')
    category = models.CharField(max_length=150, verbose_name='Категория')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateField(verbose_name='Дата последнего изменения', auto_now=True)
    category_product = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    views_counter = models.PositiveIntegerField(verbose_name="Счетчик просмотров", default=0)

    def __str__(self):
        """Возвращает строковое представление продукта — его название."""
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', ]
