import openpyxl
from django.core.management.base import BaseCommand
from catalog.models import Goods

class Command(BaseCommand):
    help_text = 'Команда для експорту даних з БД в Excel'

    def handle(self, *args, **options):
        print('Start exporting data to Excel')

        wb = openpyxl.Workbook()
        ws = wb.active

         ws.append(['Товар', 'Опис', 'Ціна', 'Оптова ціна', 'Категорія'])

        goods = Goods.objects.all()

        for good in goods:
            ws.append([
                good.name,
                good.description,
                good.price,
                good.price_opt,
                good.category.name if good.category else '',  # Якщо категорія відсутня, то покласти пустий рядок
            ])

        # Збереження файлу Excel
        wb.save('goods_data.xlsx')

        print('Finish exporting data to Excel')