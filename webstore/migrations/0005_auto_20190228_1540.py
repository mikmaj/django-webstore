# Generated by Django 2.1.7 on 2019-02-28 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webstore', '0004_auto_20190228_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='item_to_buy',
            field=models.ManyToManyField(to='webstore.StoreItem'),
        ),
    ]
