import uuid
from django.core.management.base import BaseCommand
from faker import Faker
from catalog.models import Tag

class Command(BaseCommand):
    help_text = 'Команда для заполнения БД'

    def handle(self, *args, **options):
        fake = Faker()
        print('Start')
        for _ in range(50):
            name = fake.company()
            print(name)
            uuid_str = str(uuid.uuid4())
            Tag.objects.create(name=name, uuid=uuid_str)
        print('Finish create tags')