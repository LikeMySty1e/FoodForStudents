# Generated by Django 3.1.7 on 2021-08-19 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210819_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='time',
            field=models.CharField(default='10 минут', max_length=50),
        ),
    ]
