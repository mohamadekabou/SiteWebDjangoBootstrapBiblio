# Generated by Django 4.1.7 on 2023-05-11 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_payment_user_delete_orderplaced_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity_stock',
            field=models.IntegerField(default=10),
        ),
    ]
