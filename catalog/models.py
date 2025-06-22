from django.db import models


# class MyModel(models.Model):
#     name = models.CharField(max_length=300)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Категория')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name', ]


class Product(models.Model):
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
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', ]

# class Author(models.Model):
#     first_name = models.CharField(max_length=150, verbose_name='Имя')
#     last_name = models.CharField(max_length=150, verbose_name='Фамилия')
#     birth_date = models.DateField(verbose_name='Дата рождения')
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
#
#     class Meta:
#         verbose_name = 'автор'
#         verbose_name_plural = 'авторы'
#         ordering = ['last_name', ]
#
#
# class Book(models.Model):
#     title = models.CharField(max_length=200, verbose_name='Название')
#     publication_date = models.DateField(verbose_name='Дата публикации')
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'книга'
#         verbose_name_plural = 'книги'
#         ordering = ['title', ]


# class Student(models.Model):
#     FIRST_YEAR = 'first'
#     SECOND_YEAR = 'second'
#     THIRD_YEAR = 'third'
#     FOURTH_YEAR = 'fourth'
#
#     YEAR_IN_SCHOOL_CHOICES = [
#         (FIRST_YEAR, 'Первый курс'),
#         (SECOND_YEAR, 'Второй курс'),
#         (THIRD_YEAR, 'Третий курс'),
#         (FOURTH_YEAR, 'Четвертый курс'),
#     ]
#
#     first_name = models.CharField(max_length=150, verbose_name='Имя')
#     last_name = models.CharField(max_length=150, verbose_name='Фамилия')
#     year = models.CharField(max_length=6, choices=YEAR_IN_SCHOOL_CHOICES, default=FIRST_YEAR, verbose_name='Курс')
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
#
#     class Meta:
#         verbose_name = 'студент'
#         verbose_name_plural = 'студенты'
#         ordering = ['last_name', ]
