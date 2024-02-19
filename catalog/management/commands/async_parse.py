import asyncio
import aiohttp
import datetime
import aiofiles
from catalog.models import Goods, Category
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from django.conf import settings
from django.utils.translation import gettext
from django.template.defaultfilters import slugify
from transliterate import translit
from asgiref.sync import sync_to_async

URL_2 = 'https://ukrzoloto.ua/'


class Command(BaseCommand):

    @staticmethod
    async def req_body(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                body = await resp.text()
                return body

    @staticmethod
    async def download_image(good_img_url, image_name):
        async with aiohttp.ClientSession() as session:
            async with session.get(good_img_url) as resp:
                img_data = await resp.read()
        image_src = f'{settings.BASE_DIR}\media\{image_name}.jpg'
        async with aiofiles.open(image_src, 'wb') as handler:
            await handler.write(img_data)
        return image_src

    @staticmethod
    def translit_word(name):
        return translit(name, 'ru', reversed=True)

     async def parse(self):

        startTime = datetime.datetime.now()
        print('Start')
        content = await self.req_body(URL_2 + '/catalog')
        bs = BeautifulSoup(content, 'html5lib')

        for item in bs.findAll('a', {'class': 'catalogue-categories__link'}):
            name = item.get_text()
            if name == 'Сертификаты':
                break
            print(name)
            activate = True
            url = str(item)
            category = await Category.objects.aget_or_create(name=name, activate=activate, url=url)
            good_url = URL_2 + item['href']
            goods_content = await self.req_body(good_url)
            bs1 = BeautifulSoup(goods_content, 'html5lib')
            goods = bs1.findAll('div', {'class': 'product-card__content'})
            for index, good_item in enumerate(goods):
                good_name = good_item.select_one('.title').get_text()
                good_img_url = good_item.select_one('.image')['src']
                good_price = good_item.select_one('.price__current span').get_text().replace(' ', '')
                price_opt = good_item.select_one('.price__old span').get_text().replace(' ', '')
                goods, created = await Goods.objects.aget_or_create(
                    category=category[0],
                    name=f'{good_name} + {index}',
                    description=self.translit_word(good_name),
                    price_opt=price_opt,
                    price=good_price,
                    activate=True,
                    # image=self.download_image(good_img_url, slugify(self.translit_word(good_name)))

                )
                print(goods, created)

        print('Used time:', datetime.datetime.now() - startTime)

    # main_loop.run_forever()

    def handle(self, *args, **options):
        main_loop = asyncio.get_event_loop()
        main_loop.run_until_complete(self.parse())
