from datetime import datetime
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Link(models.Model):
    STATUSLINK = [
        ("FA", "Завод"),
        ("RN", "Розничная сеть"),
        ("IE", "Индивидуальный предприниматель"),
    ]

    status_link = models.CharField(max_length=30, choices=STATUSLINK, verbose_name='Статус звена')
    related_link = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Ссылка на поставщика', **NULLABLE)
    name = models.CharField(max_length=100, verbose_name='Название')

    email = models.CharField(max_length=100, verbose_name='email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    num_house = models.CharField(max_length=10, verbose_name='Номер дома')

    debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Задолженность перед поставщиком', **NULLABLE)
    data_course = models.DateTimeField(default=datetime.now, verbose_name='Время создания')

    def __str__(self):
        return f"{self.status_link} - {self.name}"

    class Meta:
        verbose_name = 'Торговое звено'
        verbose_name_plural = 'Торговые звенья'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    model = models.CharField(max_length=100, verbose_name='Модель')
    data = models.DateField(verbose_name='Дата выхода продукта на рынок')
    link = models.ForeignKey(Link, on_delete=models.CASCADE, verbose_name='Звено цепи')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
