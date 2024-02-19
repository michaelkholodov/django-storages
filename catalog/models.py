from django.db import models
from djrichtextfield.models import RichTextField


class DateTimeStamp(models.Model):
    created = models.DateTimeField('Created', auto_now_add=True)
    updated = models.DateTimeField('Updated', auto_now=True)

    class Meta:
        abstract = True


class Category(DateTimeStamp):
    name = models.CharField('имя категорії', max_length=100, unique=True)
    url = models.URLField('Url', blank=True)
    email = models.EmailField('Email', blank=True)
    description = RichTextField('Опис', blank=True)
    activate = models.BooleanField('Active', default=False)

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['-name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/category_detail/{self.pk}/'


class Tag(models.Model):
    name = models.CharField('Имя тега', max_length=25, unique=True)
    uuid = models.UUIDField('UUID')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['-name']

    def __str__(self):
        return self.name


class Parametr(models.Model):
    name = models.CharField('Параметр товару', max_length=25, unique=True)

    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметри'

    def __str__(self):
        return self.name


class Goods(DateTimeStamp):
    name = models.CharField('Имя товару', max_length=100, unique=True)
    description = RichTextField('Опис', blank=True)
    price = models.FloatField('Price', default=0)
    price_opt = models.IntegerField('Opt', default=0)
    activate = models.BooleanField('Active', default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='goods')
    tags = models.ManyToManyField(Tag, related_name='goods_tag')
    image = models.ImageField('Зображення', upload_to='images/', blank=True)  # Оновлено поле на ImageField
    parametr = models.ForeignKey(Parametr, on_delete=models.CASCADE, related_name='parametr', null=True, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
        ordering = ['-name']

    def __str__(self):
        return self.name