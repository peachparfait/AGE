# Generated by Django 2.2 on 2020-03-09 04:11

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aniversary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annivapp', models.CharField(max_length=200, verbose_name='記念日')),
                ('story', models.TextField(default='そのものに対する思い出やエピソードなどを入力してください', max_length=1000, verbose_name='ストーリー')),
                ('createDate', models.DateTimeField(auto_now_add=True, verbose_name='記念日 登録日時')),
                ('updateDate', models.DateTimeField(auto_now=True, null=True, verbose_name='記念日 更新日時')),
            ],
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodcategory', models.CharField(max_length=30, verbose_name='食品カテゴリ')),
                ('createDate', models.DateTimeField(auto_now_add=True, verbose_name='食品カテゴリ 登録日時')),
                ('updateDate', models.DateTimeField(auto_now=True, null=True, verbose_name='食品カテゴリ 更新日時')),
            ],
        ),
        migrations.CreateModel(
            name='HomeElecAppCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ElecCategory', models.CharField(max_length=30, verbose_name='家電カテゴリ')),
                ('createDate', models.DateTimeField(auto_now_add=True, verbose_name='家電カテゴリ 登録日時')),
                ('updateDate', models.DateTimeField(auto_now=True, null=True, verbose_name='家電カテゴリ 更新日時')),
            ],
        ),
        migrations.CreateModel(
            name='OtherCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OtherCategory', models.CharField(max_length=30, verbose_name='その他カテゴリ')),
                ('createDate', models.DateTimeField(auto_now_add=True, verbose_name='その他カテゴリ 登録日時')),
                ('updateDate', models.DateTimeField(auto_now=True, null=True, verbose_name='その他カテゴリ 更新日時')),
            ],
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otherapp', models.CharField(max_length=200, verbose_name='家具、文房具、食器、雑貨、その他')),
                ('story', models.TextField(default='そのものに対する思い出やエピソードなどを入力してください', max_length=1000, verbose_name='ストーリー')),
                ('createDate', models.DateTimeField(auto_now_add=True, verbose_name='その他 登録日時')),
                ('updateDate', models.DateTimeField(auto_now=True, null=True, verbose_name='その他 更新日時')),
                ('OtherCategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='age.OtherCategory')),
            ],
        ),
        migrations.CreateModel(
            name='HomeElecApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HomeElecApp', models.CharField(max_length=200, verbose_name='家電')),
                ('story', models.TextField(default='そのものに対する思い出やエピソードなどを入力してください', max_length=1000, verbose_name='ストーリー')),
                ('createDate', models.DateTimeField(auto_now_add=True, verbose_name='家電 登録日時')),
                ('updateDate', models.DateTimeField(auto_now=True, null=True, verbose_name='家電 更新日時')),
                ('ElecCategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='age.HomeElecAppCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodname', models.CharField(max_length=200, verbose_name='食品名')),
                ('createDate', models.DateTimeField(auto_now_add=True, verbose_name='食品 登録日時')),
                ('updateDate', models.DateTimeField(auto_now=True, null=True, verbose_name='食品 更新日時')),
                ('foodcategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='age.FoodCategory')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('birthday', models.DateField(blank=True, null=True)),
                ('gender', models.IntegerField(choices=[(0, '男性'), (1, '女性'), (2, '不明')], default=2, verbose_name='性別')),
                ('rebviewStar', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True, verbose_name='レビュー星')),
                ('rebviewComment', models.TextField(null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]