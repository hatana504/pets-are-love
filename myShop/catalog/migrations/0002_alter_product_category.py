# Generated by Django 4.1.5 on 2023-04-11 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='0000000', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='catalog.category'),
        ),
    ]
