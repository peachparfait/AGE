# Generated by Django 2.2 on 2020-02-28 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('age', '0002_auto_20200228_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aniversary',
            name='story',
            field=models.TextField(default='そのものに対する思い出やエピソードなどを入力してください', max_length=1000, verbose_name='ストーリー'),
        ),
        migrations.AlterField(
            model_name='homeelecapp',
            name='story',
            field=models.TextField(default='そのものに対する思い出やエピソードなどを入力してください', max_length=1000, verbose_name='ストーリー'),
        ),
    ]
