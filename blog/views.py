from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.views import View
from blog.models import Blog


class BlogListView(ListView):
    """Представление для отображения списка всех блогов.
       Отображает все объекты модели Blog в шаблоне 'blog/blog_list.html'."""
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'


class BlogCreateView(CreateView):
    """Представление для создания нового блога.
       После успешного создания перенаправляет на список блогов."""
    model = Blog
    template_name = 'blog/blog_form.html'
    fields = ['title', 'description', 'image', 'is_published']
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(UpdateView):
    """Представление для редактирования существующего блога.
       После успешного обновления перенаправляет на страницу деталей обновлённого блога."""
    model = Blog
    template_name = 'blog/blog_form.html'
    fields = ['title', 'description', 'image', 'is_published']
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        """Возвращает URL для перенаправления после успешного обновления."""
        return reverse('blog:blog_detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    """Представление для удаления блога."""
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:blog_list')


class BlogDetailView(DetailView):
    """Представление для отображения деталей одного блога.
       Увеличивает счётчик просмотров при каждом запросе."""
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        """метод получения объекта для увеличения счётчика просмотров"""
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object
