# Generated by Django 4.2.5 on 2023-10-05 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_cidade_is_capital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidade',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
