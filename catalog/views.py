from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.urls import reverse
from catalog.models import Product
from django.views import View


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'image', 'price', 'category_product', ]
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(is_published=True)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'category', 'price', 'image']
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        return reverse('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')


def home_html(request):
    return render(request, 'catalog/home.html')


class ContactsView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')

    def post(self, request):
        name = request.POST.get("name")
        message = request.POST.get("massage")

        return HttpResponse(f"Спасибо, {name}! Сообщение принято.")



# def contacts_post(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         massage = request.POST.get("massage")
#
#         return HttpResponse(f"Спасибо, {name}! Сообщение принято.")
#     return render(request, 'catalog/contacts.html')


# def index(request):
#     product = Product.objects.get(id=1)
#     context = {
#         'product_name': product.name,
#         'product_price': product.price,
#     }
#     return render(request, 'catalog/index.html', context=context)
#
#
# def product_detail(request, product_id):
#     product = Product.objects.get(id=product_id)
#     context = {
#         'product': product,
#     }
#     return render(request, 'catalog/product_detail.html', context=context)
#
#
# def product_list(requests):
#     product = Product.objects.all()
#     context = {
#         'product': product,
#     }
#     return render(requests, 'catalog/product_list.html', context=context)
