# Generated by Django 5.0.3 on 2024-03-08 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise_api', '0002_warehousesmodel_added_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='product_code',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='product_qty',
            field=models.IntegerField(default=30),
            preserve_default=False,
        ),
    ]