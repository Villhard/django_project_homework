from django.core.management.base import BaseCommand
from faker import Faker

from store.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker(locale="ru_RU")

        for _ in range(10):
            category = Category.objects.create(
                name=fake.word(),
                description=fake.sentence(nb_words=10)
            )
            for _ in range(10):
                Product.objects.create(
                    name=fake.word(),
                    description=fake.sentence(nb_words=10),
                    price=fake.random_int(min=100, max=1000),
                    category=category
                )

        self.stdout.write(
            self.style.SUCCESS("База данных заполнена успешно")
        )
