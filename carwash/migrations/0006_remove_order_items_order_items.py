# Generated by Django 4.0.3 on 2022-04-30 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carwash', '0005_remove_item_user_item_resturant_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(related_name='order_items', to='carwash.item'),
        ),
    ]
