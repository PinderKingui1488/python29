from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'add bl'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        Product.objects.create(name="test", description="test", price="228", created_at="1488-52-69", updated_at="8841-25-96")