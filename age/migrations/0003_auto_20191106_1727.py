# Generated by Django 2.2 on 2019-11-06 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('age', '0002_remove_user_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.IntegerField(choices=[(1, '男性'), (2, '女性'), (3, 'その他')], verbose_name='性別'),
        ),
    ]
