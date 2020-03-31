from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime
from django.db.models import Count
import os

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

	reviewStar = models.IntegerField(
		verbose_name = "レビュー星",
		choices = REVIEW_STAR_CHOICES,
		null=True
	)

	reviewComment = models.TextField(null=True)

class FurnHistory(models.Model):
	history1 = models.TextField(max_length=100,default='',null=True,blank=True)
	history2 = models.TextField(max_length=100,default='',null=True,blank=True)
	history3 = models.TextField(max_length=100,default='',null=True,blank=True)
	history4 = models.TextField(max_length=100,default='',null=True,blank=True)
	history5 = models.TextField(max_length=100,default='',null=True,blank=True)
	history6 = models.TextField(max_length=100,default='',null=True,blank=True)
	history7 = models.TextField(max_length=100,default='',null=True,blank=True)
	history8 = models.TextField(max_length=100,default='',null=True,blank=True)
	history9 = models.TextField(max_length=100,default='',null=True,blank=True)
	history10 = models.TextField(max_length=100,default='',null=True,blank=True)
	historyday1 = models.DateField(default=datetime.date.today())
	historyday2 = models.DateField(default=datetime.date.today())
	historyday3 = models.DateField(default=datetime.date.today())
	historyday4 = models.DateField(default=datetime.date.today())
	historyday5 = models.DateField(default=datetime.date.today())
	historyday6 = models.DateField(default=datetime.date.today())
	historyday7 = models.DateField(default=datetime.date.today())
	historyday8 = models.DateField(default=datetime.date.today())
	historyday9 = models.DateField(default=datetime.date.today())
	historyday10 = models.DateField(default=datetime.date.today())
	mdl = models.IntegerField(primary_key=True,default=0)

#class History(models.Model):
#	history1 = models.TextField(max_length=100,default='',null=True,blank=True)
#	history2 = models.TextField(max_length=100,default='',null=True,blank=True)
#	history3 = models.TextField(max_length=100,default='',null=True,blank=True)
#	history4 = models.TextField(max_length=100,default='',null=True,blank=True)
#	history5 = models.TextField(max_length=100,default='',null=True,blank=True)
#	history6 = models.TextField(max_length=100,default='',null=True,blank=True)
#	history7 = models.TextField(max_length=100,default='',null=True,blank=True)
#	history8 = models.TextField(max_length=100,default='',null=True,blank=True)
#	history9 = models.TextField(max_length=100,default='',null=True,blank=True)
#	history10 = models.TextField(max_length=100,default='',null=True,blank=True)
#	historyday1 = models.DateField(default=datetime.date.today())
#	historyday2 = models.DateField(default=datetime.date.today())
#	historyday3 = models.DateField(default=datetime.date.today())
#	historyday4 = models.DateField(default=datetime.date.today())
#	historyday5 = models.DateField(default=datetime.date.today())
#	historyday6 = models.DateField(default=datetime.date.today())
#	historyday7 = models.DateField(default=datetime.date.today())
#	historyday8 = models.DateField(default=datetime.date.today())
#	historyday9 = models.DateField(default=datetime.date.today())
#	historyday10 = models.DateField(default=datetime.date.today())
#
#class Image(models.Model):
#	picture2 = models.ImageField(upload_to='images/',null=True,blank=True)
#	picture3 = models.ImageField(upload_to='images/',null=True,blank=True)
#	picture4 = models.ImageField(upload_to='images/',null=True,blank=True)
#	picture5 = models.ImageField(upload_to='images/',null=True,blank=True)
#	picture6 = models.ImageField(upload_to='images/',null=True,blank=True)
#	picture7 = models.ImageField(upload_to='images/',null=True,blank=True)
#	picture8 = models.ImageField(upload_to='images/',null=True,blank=True)
#	picture9 = models.ImageField(upload_to='images/',null=True,blank=True)
#	picture10 = models.ImageField(upload_to='images/',null=True,blank=True)

class ElecHistory(models.Model):
	history1 = models.TextField(max_length=100,default='',null=True,blank=True)
	history2 = models.TextField(max_length=100,default='',null=True,blank=True)
	history3 = models.TextField(max_length=100,default='',null=True,blank=True)
	history4 = models.TextField(max_length=100,default='',null=True,blank=True)
	history5 = models.TextField(max_length=100,default='',null=True,blank=True)
	history6 = models.TextField(max_length=100,default='',null=True,blank=True)
	history7 = models.TextField(max_length=100,default='',null=True,blank=True)
	history8 = models.TextField(max_length=100,default='',null=True,blank=True)
	history9 = models.TextField(max_length=100,default='',null=True,blank=True)
	history10 = models.TextField(max_length=100,default='',null=True,blank=True)
	historyday1 = models.DateField(default=datetime.date.today())
	historyday2 = models.DateField(default=datetime.date.today())
	historyday3 = models.DateField(default=datetime.date.today())
	historyday4 = models.DateField(default=datetime.date.today())
	historyday5 = models.DateField(default=datetime.date.today())
	historyday6 = models.DateField(default=datetime.date.today())
	historyday7 = models.DateField(default=datetime.date.today())
	historyday8 = models.DateField(default=datetime.date.today())
	historyday9 = models.DateField(default=datetime.date.today())
	historyday10 = models.DateField(default=datetime.date.today())
	mdl = models.IntegerField(primary_key=True,default=0)

class AnivHistory(models.Model):
	history1 = models.TextField(max_length=100,default='',null=True,blank=True)
	history2 = models.TextField(max_length=100,default='',null=True,blank=True)
	history3 = models.TextField(max_length=100,default='',null=True,blank=True)
	history4 = models.TextField(max_length=100,default='',null=True,blank=True)
	history5 = models.TextField(max_length=100,default='',null=True,blank=True)
	history6 = models.TextField(max_length=100,default='',null=True,blank=True)
	history7 = models.TextField(max_length=100,default='',null=True,blank=True)
	history8 = models.TextField(max_length=100,default='',null=True,blank=True)
	history9 = models.TextField(max_length=100,default='',null=True,blank=True)
	history10 = models.TextField(max_length=100,default='',null=True,blank=True)
	historyday1 = models.DateField(default=datetime.date.today())
	historyday2 = models.DateField(default=datetime.date.today())
	historyday3 = models.DateField(default=datetime.date.today())
	historyday4 = models.DateField(default=datetime.date.today())
	historyday5 = models.DateField(default=datetime.date.today())
	historyday6 = models.DateField(default=datetime.date.today())
	historyday7 = models.DateField(default=datetime.date.today())
	historyday8 = models.DateField(default=datetime.date.today())
	historyday9 = models.DateField(default=datetime.date.today())
	historyday10 = models.DateField(default=datetime.date.today())
	mdl = models.IntegerField(primary_key=True,default=0)

class ClothHistory(models.Model):
	history1 = models.TextField(max_length=100,default='',null=True,blank=True)
	history2 = models.TextField(max_length=100,default='',null=True,blank=True)
	history3 = models.TextField(max_length=100,default='',null=True,blank=True)
	history4 = models.TextField(max_length=100,default='',null=True,blank=True)
	history5 = models.TextField(max_length=100,default='',null=True,blank=True)
	history6 = models.TextField(max_length=100,default='',null=True,blank=True)
	history7 = models.TextField(max_length=100,default='',null=True,blank=True)
	history8 = models.TextField(max_length=100,default='',null=True,blank=True)
	history9 = models.TextField(max_length=100,default='',null=True,blank=True)
	history10 = models.TextField(max_length=100,default='',null=True,blank=True)
	historyday1 = models.DateField(default=datetime.date.today())
	historyday2 = models.DateField(default=datetime.date.today())
	historyday3 = models.DateField(default=datetime.date.today())
	historyday4 = models.DateField(default=datetime.date.today())
	historyday5 = models.DateField(default=datetime.date.today())
	historyday6 = models.DateField(default=datetime.date.today())
	historyday7 = models.DateField(default=datetime.date.today())
	historyday8 = models.DateField(default=datetime.date.today())
	historyday9 = models.DateField(default=datetime.date.today())
	historyday10 = models.DateField(default=datetime.date.today())
	mdl = models.IntegerField(primary_key=True,default=0)

class OtherHistory(models.Model):
	history1 = models.TextField(max_length=100,default='',null=True,blank=True)
	history2 = models.TextField(max_length=100,default='',null=True,blank=True)
	history3 = models.TextField(max_length=100,default='',null=True,blank=True)
	history4 = models.TextField(max_length=100,default='',null=True,blank=True)
	history5 = models.TextField(max_length=100,default='',null=True,blank=True)
	history6 = models.TextField(max_length=100,default='',null=True,blank=True)
	history7 = models.TextField(max_length=100,default='',null=True,blank=True)
	history8 = models.TextField(max_length=100,default='',null=True,blank=True)
	history9 = models.TextField(max_length=100,default='',null=True,blank=True)
	history10 = models.TextField(max_length=100,default='',null=True,blank=True)
	historyday1 = models.DateField(default=datetime.date.today())
	historyday2 = models.DateField(default=datetime.date.today())
	historyday3 = models.DateField(default=datetime.date.today())
	historyday4 = models.DateField(default=datetime.date.today())
	historyday5 = models.DateField(default=datetime.date.today())
	historyday6 = models.DateField(default=datetime.date.today())
	historyday7 = models.DateField(default=datetime.date.today())
	historyday8 = models.DateField(default=datetime.date.today())
	historyday9 = models.DateField(default=datetime.date.today())
	historyday10 = models.DateField(default=datetime.date.today())
	mdl = models.IntegerField(primary_key=True,default=0)
#Furnモデルを作成
class Furn(models.Model):
	name = models.CharField('家具名',max_length=200)
	story = models.TextField('ストーリー',max_length=1000,default='')
	birthday = models.DateField('誕生日（購入日など）',default=datetime.date.today())
	favorite = models.IntegerField('お気に入り度',validators=[MinValueValidator(0),MaxValueValidator(10)],default=0)
	createDate = models.DateTimeField('家具 登録日時', auto_now_add = True)
	updateDate = models.DateTimeField('家具 更新日時', auto_now = True, blank=True, null=True)
	picture1 = models.ImageField('写真',upload_to='images/',null=True,blank=True)
	picture2 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture3 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture4 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture5 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture6 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture7 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture8 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture9 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture10 = models.ImageField(upload_to='images/',null=True,blank=True)
	#picture=models.ForeignKey(Image,on_delete=models.PROTECT,verbose_name="画像",default=1)
	#history=models.ForeignKey(History,on_delete=models.PROTECT,verbose_name="ヒストリー",default=1)
	def __str__(self):
		return self.name



# HomeElecAppCategoryモデルを作成
class HomeElecAppCategory(models.Model):
    ElecCategory = models.CharField('家電カテゴリ',max_length=30)

    createDate = models.DateTimeField('家電カテゴリ 登録日時', auto_now_add = True)
    updateDate = models.DateTimeField('家電カテゴリ 更新日時', auto_now = True, blank=True, null=True)

    def __str__(self):
            return self.ElecCategory

# HomeElecAppモデルを作成
class HomeElecApp(models.Model):
	name = models.CharField('家電名',max_length=200)
	category = models.ForeignKey(HomeElecAppCategory,on_delete=models.PROTECT,verbose_name="家電の種類",default=1)
	story = models.TextField('ストーリー',max_length=1000,default='')
	birthday = models.DateField('誕生日（購入日など）',default=datetime.date.today())
	createDate = models.DateTimeField('家電 登録日時', auto_now_add = True)
	updateDate = models.DateTimeField('家電 更新日時', auto_now = True, blank=True, null=True)
	favorite = models.IntegerField('お気に入り度',validators=[MinValueValidator(0),MaxValueValidator(10)],default=0)
	picture1 = models.ImageField('写真',upload_to='images/',null=True,blank=True)
	picture2 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture3 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture4 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture5 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture6 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture7 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture8 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture9 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture10 = models.ImageField(upload_to='images/',null=True,blank=True)
	#picture=models.ForeignKey(Image,on_delete=models.PROTECT,verbose_name="画像",default=1)
	#history=models.ForeignKey(History,on_delete=models.PROTECT,verbose_name="ヒストリー",default=1)
	def __str__(self):
     	    return self.name

class Aniversary(models.Model):
	annivapp = models.CharField('記念日名',max_length=200)
	story = models.TextField('ストーリー',max_length=1000,default='')
	didday = models.DateField('記念日が起こった日付',default=datetime.date.today())
	createDate = models.DateTimeField('記念日 登録日時', auto_now_add = True)
	updateDate = models.DateTimeField('記念日 更新日時', auto_now = True, blank=True, null=True)
	favorite = models.IntegerField('お気に入り度',validators=[MinValueValidator(0),MaxValueValidator(10)],default=0)
	picture1 = models.ImageField('写真',upload_to='images/',null=True,blank=True)
	picture2 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture3 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture4 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture5 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture6 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture7 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture8 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture9 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture10 = models.ImageField(upload_to='images/',null=True,blank=True)
	#picture=models.ForeignKey(Image,on_delete=models.PROTECT,verbose_name="画像",default=1)
	#history=models.ForeignKey(History,on_delete=models.PROTECT,verbose_name="ヒストリー",default=1)
	def __str__(self):
     	    return self.annivapp

class OtherCategory(models.Model):
    othercategory = models.CharField('その他カテゴリ',max_length=30)

    createDate = models.DateTimeField('その他カテゴリ 登録日時', auto_now_add = True)
    updateDate = models.DateTimeField('その他カテゴリ 更新日時', auto_now = True, blank=True, null=True)

    def __str__(self):
            return self.othercategory
class Other(models.Model):
	name = models.CharField('名前',max_length=200)
	category = models.ForeignKey(OtherCategory,on_delete=models.PROTECT,verbose_name="種類",default=1)
	story = models.TextField('ストーリー',max_length=1000,default='')
	birthday = models.DateField('誕生日（購入日など）',default=datetime.date.today())
	createDate = models.DateTimeField('その他 登録日時', auto_now_add = True)
	updateDate = models.DateTimeField('その他 更新日時', auto_now = True, blank=True, null=True)
	favorite = models.IntegerField('お気に入り度',validators=[MinValueValidator(0),MaxValueValidator(10)],default=0)
	picture1 = models.ImageField('写真',upload_to='images/',null=True,blank=True)
	picture2 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture3 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture4 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture5 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture6 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture7 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture8 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture9 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture10 = models.ImageField(upload_to='images/',null=True,blank=True)
	#picture=models.ForeignKey(Image,on_delete=models.PROTECT,verbose_name="画像",default=1)
	#history=models.ForeignKey(History,on_delete=models.PROTECT,verbose_name="ヒストリー",default=1)
	def __str__(self):
     	    return self.name
class ClothCategory(models.Model):
    fashioncategory = models.CharField('ファッションカテゴリ',max_length=30)

    createDate = models.DateTimeField(' 登録日時', auto_now_add = True)
    updateDate = models.DateTimeField(' 更新日時', auto_now = True, blank=True, null=True)

    def __str__(self):
            return self.fashioncategory
class Clothes(models.Model):
	name = models.CharField('名前',max_length=200)
	category = models.ForeignKey(ClothCategory,on_delete=models.PROTECT,verbose_name="ファッションの種類",default=1)
	story = models.TextField('ストーリー',max_length=1000,default='')
	birthday = models.DateField('誕生日（購入日など）',default=datetime.date.today())
	createDate = models.DateTimeField('ファッション 登録日時', auto_now_add = True)
	updateDate = models.DateTimeField('ファッション 更新日時', auto_now = True, blank=True, null=True)
	favorite = models.IntegerField('お気に入り度',validators=[MinValueValidator(0),MaxValueValidator(10)],default=0)
	picture1 = models.ImageField('写真',upload_to='images/',null=True,blank=True)
	picture2 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture3 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture4 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture5 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture6 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture7 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture8 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture9 = models.ImageField(upload_to='images/',null=True,blank=True)
	picture10 = models.ImageField(upload_to='images/',null=True,blank=True)
	#picture=models.ForeignKey(Image,on_delete=models.PROTECT,verbose_name="画像",default=1)
	#history=models.ForeignKey(History,on_delete=models.PROTECT,verbose_name="ヒストリー",default=1)
	def __str__(self):
     	    return self.name
