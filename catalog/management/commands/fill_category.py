from django.core.management.base import BaseCommand
from faker import Faker
from catalog.models import Category

class Command(BaseCommand):
    help_text = 'Команда для заполнения БД'

    def handle(self, *args, **options):
        fake = Faker()
        print('Start')
        for _ in range(15):
            Category.objects.get_or_create(
                name=fake.job(),
                url=fake.uri(),
                description=fake.paragraph(nb_sentences=3),
                activate=fake.pybool(),
            )
        print('Finish')