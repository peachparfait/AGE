# Generated by Django 2.2 on 2020-04-15 11:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('age', '0005_auto_20200411_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='aniversary',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='clothes',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='furn',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='homeelecapp',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='other',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='aniversary',
            name='didday',
            field=models.DateField(default=datetime.date(2020, 4, 15), verbose_name='記念日が起こった日付'),
        ),
        migrations.AlterField(
            model_name='anivhistory',
            name='historyday1',
            field=models.DateField(default=datetime.date(2020, 4, 15), verbose_name='出来事の日付'),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='birthday',
            field=models.DateField(default=datetime.date(2020, 4, 15), verbose_name='誕生日（購入日など）'),
        ),
        migrations.AlterField(
            model_name='clothhistory',
            name='historyday1',
            field=models.DateField(default=datetime.date(2020, 4, 15), verbose_name='出来事の日付'),
        ),
        migrations.AlterField(
            model_name='elechistory',
            name='historyday1',
            field=models.DateField(default=datetime.date(2020, 4, 15), verbose_name='出来事の日付'),
        ),
        migrations.AlterField(
            model_name='furn',
            name='birthday',
            field=models.DateField(default=datetime.date(2020, 4, 15), verbose_name='誕生日（購入日など）'),
        ),
        migrations.AlterField(
            model_name='furnhistory',
            name='historyday1',
            field=models.DateField(default=datetime.date(2020, 4, 15), verbose_name='出来事の日付'),
        ),
        migrations.AlterField(
            model_name='homeelecapp',
            name='birthday',
            field=models.DateField(default=datetime.date(2020, 4, 15), verbose_name='誕生日（購入日など）'),
        ),
        migrations.AlterField(
            model_name='other',
            name='birthday',
            field=models.DateField(default=datetime.date(2020, 4, 15), verbose_name='誕生日（購入日など）'),
        ),
        migrations.AlterField(
            model_name='otherhistory',
            name='historyday1',
            field=models.DateField(default=datetime.date(2020, 4, 15), verbose_name='出来事の日付'),
        ),
    ]