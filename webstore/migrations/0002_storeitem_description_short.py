# Generated by Django 2.1.7 on 2019-02-27 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeitem',
            name='description_short',
            field=models.CharField(default='asd', max_length=150),
            preserve_default=False,
        ),
    ]
