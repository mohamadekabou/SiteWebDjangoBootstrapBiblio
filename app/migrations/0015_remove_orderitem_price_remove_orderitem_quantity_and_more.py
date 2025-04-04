# Generated by Django 4.1.7 on 2023-05-17 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='price',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='total_cost',
            field=models.FloatField(default=40),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='nbrJour',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
