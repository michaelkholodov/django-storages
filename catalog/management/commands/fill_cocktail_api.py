import random
import requests
from django.core.management.base import BaseCommand
from catalog.models import Category, Goods

class Command(BaseCommand):
    help_text = 'Команда для заповнення БД'

    API_URL = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita'

    def handle(self, *args, **options):
        print('Start')

        response = requests.get(self.API_URL)

        if response.status_code == 200:
            data = response.json()
            drinks = data.get('drinks', [])

            for drink_data in drinks:
                cat_name = drink_data.get('strCategory')
                print(f'Категорія: {cat_name}')
                category, created = Category.objects.get_or_create(
                    name=cat_name,

                )

                goods_name = drink_data.get('strDrink')
                print(f'Товар: {goods_name}')
                Goods.objects.create(
                    name=goods_name,
                    description=drink_data.get('strInstructions'),
                    price=random.uniform(150, 2000),
                    price_opt=random.randint(300, 1088),
                    activate=True,
                    category=category,
                    image=drink_data.get('strDrinkThumb'),
                )

        else:
            print('Failed to fetch data from API')

        print('Finish')