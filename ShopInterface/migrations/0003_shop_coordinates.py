# Generated by Django 2.2.4 on 2019-08-12 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopInterface', '0002_auto_20190811_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='coordinates',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]
