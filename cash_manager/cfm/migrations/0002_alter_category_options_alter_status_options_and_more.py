# Generated by Django 4.2.20 on 2025-03-22 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cfm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория',
                     'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Статус',
                     'verbose_name_plural': 'Статусы'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'Подкатегория',
                     'verbose_name_plural': 'Подкатегории'},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': [
                'created_at'], 'verbose_name': 'Транзакция', 'verbose_name_plural': 'Транзакции'},
        ),
        migrations.AlterModelOptions(
            name='transactiontype',
            options={'verbose_name': 'Тип транзакции',
                     'verbose_name_plural': 'Типы транзакции'},
        ),
    ]
