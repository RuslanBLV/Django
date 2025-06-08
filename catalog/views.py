from django.shortcuts import render
from django.http import HttpResponse


def home_html(request):
    return render(request, 'catalog/home.html')


def contacts_post(request):
    if request.method == "POST":
        name = request.POST.get("name")
        massage = request.POST.get("massage")
        return HttpResponse(f"Спасибо, {name}! Сообщение принято.")
    return render(request, 'catalog/contacts.html')
