from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Product


def home_html(request):
    return render(request, 'catalog/home.html')


def contacts_post(request):
    if request.method == "POST":
        name = request.POST.get("name")
        massage = request.POST.get("massage")

        return HttpResponse(f"Спасибо, {name}! Сообщение принято.")
    return render(request, 'catalog/contacts.html')


def index(request):
    product = Product.objects.get(id=1)
    context = {
        'product_name': product.name,
        'product_price': product.price,
    }
    return render(request, 'catalog/index.html', context=context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'catalog/product_detail.html', context=context)


def product_list(requests):
    product = Product.objects.all()
    context = {
        'product': product,
    }
    return render(requests, 'catalog/product_list.html', context=context)
