from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.urls import reverse
from catalog.models import Product
from django.views import View
from catalog.forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseForbidden


class UnPublishProductView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав для публикации продукта.")

        product.unpublish = True
        product.save()

        return redirect('catalog:product_detail', pk=product_id)


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Представление для создания нового продукта"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.add_product'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Представление для отображения списка опубликованных продуктов."""
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    permission_required = 'catalog.view_product'

    def get_queryset(self):
        """фильтрация только опубликованных продуктов."""
        return Product.objects.filter(unpublish=True)


class ProductDetailView(LoginRequiredMixin, DetailView):
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['is_moderator'] = user.groups.filter(name='moderators').exists() if user.is_authenticated else False
        return context


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Представление для редактирования продукта"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    permission_required = 'catalog.change_product'

    def get_queryset(self):
        """Ограничиваем обновление только продуктами владельца"""
        return Product.objects.filter(owner=self.request.user)

    def get_success_url(self):
        """Возвращает URL для перенаправления после успешного обновления — страницу деталей продукта."""
        return reverse('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Представление для удаления продукта"""
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.delete_product'

    def dispatch(self, request, *args, **kwargs):
        """Проверяем, является ли пользователь владельцем или модератором"""
        obj = self.get_object()
        user = request.user

        is_moderator = user.groups.filter(name='moderators').exists()

        if obj.owner != user and not is_moderator:
            return HttpResponseForbidden('Удалять продукт может только владелец или модератор')

        return super().dispatch(request, *args, **kwargs)


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
