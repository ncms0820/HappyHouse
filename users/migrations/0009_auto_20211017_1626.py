# Generated by Django 3.2.8 on 2021-10-17 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_type_product'),
        ('users', '0008_alter_user_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='appartment',
            field=models.CharField(blank=True, choices=[('a1', 'A1'), ('a2', 'A2'), ('a3', 'A3'), ('b1', 'B1'), ('b1', 'B2'), ('b1', 'B3'), ('b1', 'C1'), ('b1', 'C2'), ('b1', 'C3')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='cart',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]
