# Generated by Django 4.2.9 on 2024-01-14 13:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_link', models.CharField(choices=[('FA', 'Завод'), ('RN', 'Розничная сеть'), ('IE', 'Индивидуальный предприниматель')], max_length=30, verbose_name='Статус звена')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('num_house', models.CharField(max_length=10, verbose_name='Номер дома')),
                ('debt', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Задолженность перед поставщиком')),
                ('data_course', models.DateTimeField(default=datetime.datetime.now, verbose_name='Время создания')),
                ('related_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_link.link', verbose_name='Ссылка на поставщика')),
            ],
            options={
                'verbose_name': 'Торговое звено',
                'verbose_name_plural': 'Торговые звенья',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('data', models.DateField(verbose_name='Дата выхода продукта на рынок')),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_link.link', verbose_name='Звено цепи')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
