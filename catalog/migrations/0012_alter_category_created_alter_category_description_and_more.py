# Generated by Django 4.2.7 on 2024-02-18 22:30

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=djrichtextfield.models.RichTextField(blank=True, verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='description',
            field=djrichtextfield.models.RichTextField(blank=True, verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Зображення'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Имя товару'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
    ]
