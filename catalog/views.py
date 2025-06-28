from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.urls import reverse
from catalog.models import Product
from django.views import View


class ProductCreateView(CreateView):
    """Представление для создания нового продукта"""
    model = Product
    fields = ['name', 'description', 'image', 'price', 'category_product', 'views_counter',]
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductListView(ListView):
    """Представление для отображения списка опубликованных продуктов."""
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        """фильтрация только опубликованных продуктов."""
        return Product.objects.filter(is_published=True)


class ProductDetailView(DetailView):
    """Представление для отображения деталей одного продукта."""
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        """метод получения объекта для увеличения счётчика просмотров"""
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductUpdateView(UpdateView):
    """Представление для редактирования продукта"""
    model = Product
    fields = ['name', 'description', 'category', 'price', 'image']
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        """Возвращает URL для перенаправления после успешного обновления — страницу деталей продукта."""
        return reverse('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    """Представление для удаления продукта"""
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')


def home_html(request):
    """Функция-представление для главной страницы.
       Просто рендерит шаблон 'catalog/home.html'"""
    return render(request, 'catalog/home.html')


class ContactsView(View):
    """Страница контактов"""
    def get(self, request):
        """Обрабатывает GET-запрос, отображая форму контактов."""
        return render(request, 'catalog/contacts.html')

    def post(self, request):
        """Обрабатывает POST-запрос, принимает данные формы и возвращает сообщение"""
        name = request.POST.get("name")
        message = request.POST.get("massage")

        return HttpResponse(f"Спасибо, {name}! Сообщение принято.")
