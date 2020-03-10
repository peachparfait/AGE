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




#Furnモデルを作成
class Furn(models.Model):
	furnname = models.CharField('家具名',max_length=200)
	story = models.TextField('ストーリー',max_length=1000,default='')
	favorite = models.IntegerField('お気に入り度',validators=[MinValueValidator(0),MaxValueValidator(10)],default=0)
	createDate = models.DateTimeField('家具 登録日時', auto_now_add = True)
	updateDate = models.DateTimeField('家具 更新日時', auto_now = True, blank=True, null=True)



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
	story = models.TextField('ストーリー',max_length=1000,default='')
	createDate = models.DateTimeField('家電 登録日時', auto_now_add = True)
	updateDate = models.DateTimeField('家電 更新日時', auto_now = True, blank=True, null=True)
	favorite = models.IntegerField('お気に入り度',validators=[MinValueValidator(0),MaxValueValidator(10)],default=0)
	def __str__(self):
     	    return self.HomeElecApp

class Aniversary(models.Model):
	annivapp = models.CharField('記念日名',max_length=200)
	story = models.TextField('ストーリー',max_length=1000,default='')
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
	story = models.TextField('ストーリー',max_length=1000,default='')
	createDate = models.DateTimeField('その他 登録日時', auto_now_add = True)
	updateDate = models.DateTimeField('その他 更新日時', auto_now = True, blank=True, null=True)
	favorite = models.IntegerField('お気に入り度',validators=[MinValueValidator(0),MaxValueValidator(10)],default=0)
	def __str__(self):
     	    return self.otherapp
class ClothCategory(models.Model):
    fashioncategory = models.CharField('ファッションカテゴリ',max_length=30)

    createDate = models.DateTimeField(' 登録日時', auto_now_add = True)
    updateDate = models.DateTimeField(' 更新日時', auto_now = True, blank=True, null=True)

    def __str__(self):
            return self.fashioncategory
class Clothes(models.Model):
	fashionapp = models.CharField('名前',max_length=200)
	fashioncategory = models.ForeignKey(ClothCategory,on_delete=models.PROTECT)
	story = models.TextField('ストーリー',max_length=1000,default='')
	createDate = models.DateTimeField('ファッション 登録日時', auto_now_add = True)
	updateDate = models.DateTimeField('ファッション 更新日時', auto_now = True, blank=True, null=True)
	favorite = models.IntegerField('お気に入り度',validators=[MinValueValidator(0),MaxValueValidator(10)],default=0)
	def __str__(self):
     	    return self.fashionapp
#TODO:HTMLとかviewsとかurlsにもその他追加＆年齢を追加できるように！
