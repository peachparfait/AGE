# Generated by Django 2.2 on 2020-03-09 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('age', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='other',
            old_name='OtherCategory',
            new_name='othercategory',
        ),
        migrations.RenameField(
            model_name='othercategory',
            old_name='OtherCategory',
            new_name='othercategory',
        ),
    ]