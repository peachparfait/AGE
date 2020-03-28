# Generated by Django 2.2 on 2020-03-28 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('age', '0019_auto_20200328_0021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anivhistory',
            name='id',
        ),
        migrations.RemoveField(
            model_name='clothhistory',
            name='id',
        ),
        migrations.RemoveField(
            model_name='elechistory',
            name='id',
        ),
        migrations.RemoveField(
            model_name='furnhistory',
            name='id',
        ),
        migrations.RemoveField(
            model_name='otherhistory',
            name='id',
        ),
        migrations.AddField(
            model_name='anivhistory',
            name='mdl',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='clothhistory',
            name='mdl',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='elechistory',
            name='mdl',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='furnhistory',
            name='mdl',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='otherhistory',
            name='mdl',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
