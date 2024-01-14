# Generated by Django 4.2.9 on 2024-01-14 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_link', '0003_alter_product_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='related_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_link.link', verbose_name='Ссылка на поставщика'),
        ),
        migrations.AlterField(
            model_name='link',
            name='debt',
            field=models.IntegerField(blank=True, null=True, verbose_name='Задолженность перед поставщиком'),
        ),
    ]
