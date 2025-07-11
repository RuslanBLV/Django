from django import forms
from .models import Product
from django.core.exceptions import ValidationError
from users.models import CustomUser


error_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category', 'category_product',]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название продукта'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание продукта'
        })
        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену продукта'
        })
        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Впишите категорию продукта'
        })


    def clean(self):
        name = self.cleaned_data.get('name')
        description = self.cleaned_data.get('description')
        category = self.cleaned_data.get('category')

        for word in error_words:
            word_lower = word.lower()
            if name.lower() == word_lower:
                self.add_error('name', 'Некорректное слово')
            if description.lower() == word_lower:
                self.add_error('description', 'Некорректное слово')
            if category.lower() == word_lower:
                self.add_error('category', 'Некорректное слово')

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price

