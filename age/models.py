from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	birthday = models.DateField(blank=True,null=True)
	GENDER_CHOICES =(
		(0,'男性'),
		(1,'女性'),
		(2,'不明'),
	)

	gender = models.IntegerField(
		default= 2,
		verbose_name = "性別",
		choices = GENDER_CHOICES
	)

	REVIEW_STAR_CHOICES = (
		(1,'1'),
		(2,'2'),
		(3,'3'),
		(4,'4'),
		(5,'5'),
	)

	rebviewStar = models.IntegerField(
		verbose_name = "レビュー星",
		choices = REVIEW_STAR_CHOICES,
		null=True
	)

	rebviewComment = models.TextField(null=True)

# FoodCategoryモデルを作成
class FoodCategory(models.Model):
    foodcategory = models.CharField('食品カテゴリ',max_length=30)

    createDate = models.DateTimeField('食品カテゴリ 登録日時', auto_now_add = True)
    updateDate = models.DateTimeField('食品カテゴリ 更新日時', auto_now = True, blank=True, null=True)

    def __str__(self):
            return self.foodcategory


# Foodモデルを作成
class Food(models.Model):
    foodname = models.CharField('食品名',max_length=200)
    # FoodCategoryテーブルと一対多（ForeignKey）のリレーション
    foodcategory = models.ForeignKey(FoodCategory,on_delete=models.PROTECT)
    
    createDate = models.DateTimeField('食品 登録日時', auto_now_add = True)
    updateDate = models.DateTimeField('食品 更新日時', auto_now = True, blank=True, null=True)
    def __str__(self):
     	    return self.foodname

# HomeElecAppCategoryモデルを作成
class HomeElecAppCategory(models.Model):
    ElecCategory = models.CharField('家電カテゴリ',max_length=30)

    createDate = models.DateTimeField('家電カテゴリ 登録日時', auto_now_add = True)
    updateDate = models.DateTimeField('家電カテゴリ 更新日時', auto_now = True, blank=True, null=True)

    def __str__(self):
            return self.ElecCategory

# HomeElecAppモデルを作成
class HomeElecApp(models.Model):
	HomeElecApp = models.CharField('家電名',max_length=200)
	ElecCategory = models.ForeignKey(HomeElecAppCategory,on_delete=models.PROTECT)
	story = models.TextField('ストーリー',max_length=1000,default='そのものに対する思い出やエピソードなどを入力してください')
	createDate = models.DateTimeField('家電 登録日時', auto_now_add = True)
	updateDate = models.DateTimeField('家電 更新日時', auto_now = True, blank=True, null=True)
	favorite = models.IntegerField('お気に入り度',validators=[MinValueValidator(0),MaxValueValidator(10)],default=0)
	def __str__(self):
     	    return self.HomeElecApp

class Aniversary(models.Model):
	annivapp = models.CharField('記念日名',max_length=200)
	story = models.TextField('ストーリー',max_length=1000,default='そのものに対する思い出やエピソードなどを入力してください')
	createDate = models.DateTimeField('記念日 登録日時', auto_now_add = True)
	updateDate = models.DateTimeField('記念日 更新日時', auto_now = True, blank=True, null=True)
	favorite = models.IntegerField('お気に入り度',validators=[MinValueValidator(0),MaxValueValidator(10)],default=0)


class OtherCategory(models.Model):
    othercategory = models.CharField('その他カテゴリ',max_length=30)

    createDate = models.DateTimeField('その他カテゴリ 登録日時', auto_now_add = True)
    updateDate = models.DateTimeField('その他カテゴリ 更新日時', auto_now = True, blank=True, null=True)

    def __str__(self):
            return self.othercategory
class Other(models.Model):
	otherapp = models.CharField('名前',max_length=200)
	othercategory = models.ForeignKey(OtherCategory,on_delete=models.PROTECT)
	story = models.TextField('ストーリー',max_length=1000,default='そのものに対する思い出やエピソードなどを入力してください')
	createDate = models.DateTimeField('その他 登録日時', auto_now_add = True)
	updateDate = models.DateTimeField('その他 更新日時', auto_now = True, blank=True, null=True)
	favorite = models.IntegerField('お気に入り度',validators=[MinValueValidator(0),MaxValueValidator(10)],default=0)
	def __str__(self):
     	    return self.otherapp
#TODO:HTMLとかviewsとかurlsにもその他追加＆年齢を追加できるように！
