# Generated by Django 4.2.9 on 2024-01-13 08:08

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
                ('debt', models.IntegerField(verbose_name='Задолженность перед поставщиком')),
                ('data_course', models.DateTimeField(default=datetime.datetime.now, verbose_name='Время создания')),
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
                ('data', models.DateTimeField(verbose_name='Дата выхода продукта на рынок')),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_link.link', verbose_name='Звено цепи')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('num_house', models.CharField(max_length=10, verbose_name='Номер дома')),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_link.link', verbose_name='Звено цепи')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]
