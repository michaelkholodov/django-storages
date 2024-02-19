import requests
import datetime
from django.core.management.base import BaseCommand
from catalog.models import Category, Goods
from bs4 import BeautifulSoup
from django.conf import settings
from django.utils.translation import gettext
from django.template.defaultfilters import slugify
from transliterate import translit

URL = 'https://rozetka.com.ua/mobile-phones/c80003/producer=apple/'
URL_2 = 'https://ukrzoloto.ua/'

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko / 20100101 Firefox / 71.0',
            'accept': ' * / * '
         }


class Command(BaseCommand):
    help_text = 'Parse data'

    @staticmethod
    def translit_word(name):
        return translit(name, 'ru', reversed=True)


    @staticmethod
    def download_image(good_img_url, image_name):
        print(image_name)
        image_src = f'{settings.BASE_DIR}\media\{image_name}.jpg'
        img_data = requests.get(good_img_url).content
        with open(image_src, 'wb') as handler:
            handler.write(img_data)
        return image_src

    def handle(self, *args, **options):
        startTime = datetime.datetime.now()
        print('Start')
        r = requests.get(URL_2 + '/catalog')
        print(r.status_code)
        bs = BeautifulSoup(r.content, 'html5lib')

        for item in bs.findAll('a', {'class': 'catalogue-categories__link'}):
            name = item.get_text()
            if name == 'Сертификаты':
                break
            print(name)
            activate = True
            url = str(item)
            category = Category.objects.get_or_create(name=name, activate=activate, url=url)
            good_url = URL_2 + item['href']
            request = requests.get(good_url)
            bs1 = BeautifulSoup(request.content, 'html5lib')
            goods = bs1.findAll('div', {'class': 'product-card__content'})
            for index, good_item in enumerate(goods):
                good_name = good_item.select_one('.title').get_text()
                good_img_url = good_item.select_one('.image')['src']
                good_price = good_item.select_one('.price__current span').get_text().replace(' ', '')
                price_opt = good_item.select_one('.price__old span').get_text().replace(' ', '')
                goods, created = Goods.objects.get_or_create(
                    category=category[0],
                    name=f'{good_name} + {index}',
                    description=self.translit_word(good_name),
                    price_opt=price_opt,
                    price=good_price,
                    activate=True,
                    image=self.download_image(good_img_url, slugify(self.translit_word(good_name)))

                )
                print(goods, created)
        print('Used time:', datetime.datetime.now() - startTime)