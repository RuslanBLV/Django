from django.db import models


class Blog(models.Model):
    """Модель для хранения информации о блогах."""
    title = models.CharField(max_length=150, verbose_name='заголовок')
    description = models.TextField(null=True, blank=True, verbose_name='содержимое')
    image = models.ImageField(verbose_name='Изображение', upload_to='media/photos/')
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    views_counter = models.PositiveIntegerField(verbose_name="Счетчик просмотров", default=0)

    def __str__(self):
        """Возвращает строковое представление объекта — заголовок блога."""
        return self.title

    class Meta:
        """Метаданные модели Blog, включая удобочитаемые имена."""
        verbose_name = 'заголовок'
        verbose_name_plural = 'заголовки'
