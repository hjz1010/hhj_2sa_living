# Generated by Django 4.0.6 on 2022-07-20 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_price_alter_product_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='english_name',
            field=models.CharField(default='english', max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='furniture',
            name='english_name',
            field=models.CharField(default='', max_length=45),
            preserve_default=False,
        ),
    ]
