from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'add products to the database'

    def handle(self, *args, **options):
        category4, _ = Category.objects.get_or_create(name='Рыба', description='Рыбные',)

        products = [
            {'name': 'Форель', 'price': 400, "created_at": "2025-01-01", "updated_at": "2025-02-02",
             'category_product': category4},
            {'name': 'Семга', 'price': 250, "created_at": "2025-01-01", "updated_at": "2025-02-02",
             'category_product': category4}
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exist: {product.name}'))
