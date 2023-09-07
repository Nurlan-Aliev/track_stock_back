# Generated by Django 4.2.4 on 2023-09-06 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('wholesale_price', models.PositiveSmallIntegerField(null=True)),
                ('retail_price', models.PositiveSmallIntegerField(null=True)),
            ],
        ),
    ]
