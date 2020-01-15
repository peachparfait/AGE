from django.db import models
from django.utils import timezone

class User(models.Model):
        #ユーザー情報
        userID = models.CharField(max_length=50)
        userName = models.CharField(max_length=50)
        mailAddress = models.EmailField(max_length=200)
        passWord = models.CharField(max_length=128)
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
                choices = REVIEW_STAR_CHOICES
        )
        rebviewComment = models.TextField()
        createDate = models.DateTimeField('ユーザー登録日時', auto_now_add = True)
        updateDate = models.DateTimeField('ユーザー情報更新日時', auto_now = True, blank=True, null=True)
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
        homeelecappcegory = models.CharField('家電カテゴリ',max_length=30)

        createDate = models.DateTimeField('家電カテゴリ 登録日時', auto_now_add = True)
        updateDate = models.DateTimeField('家電カテゴリ 更新日時', auto_now = True, blank=True, null=True)

        def __str__(self):
            return self.homeelecappcegory

# HomeElecAppモデルを作成
class HomeElecApp(models.Model):
        homeelecapp = models.CharField('家電',max_length=200)
        homeelecategory = models.ForeignKey(HomeElecAppCategory,on_delete=models.PROTECT)
        createDate = models.DateTimeField('家電 登録日時', auto_now_add = True)
        updateDate = models.DateTimeField('家電 更新日時', auto_now = True, blank=True, null=True)
        electcreateDate = models.DateTimeField('記念日登録日時', auto_now_add = True)
        electupdateDate = models.DateTimeField('記念日更新日時', auto_now = True, blank=True, null=True)

class Aniversary(models.Model):
        #記念日
        annivID = models.CharField(max_length=50)
        annivName = models.CharField(max_length=50)
        annivcreateDate = models.DateTimeField('記念日登録日時', auto_now_add = True)
        annivupdateDate = models.DateTimeField('記念日更新日時', auto_now = True, blank=True, null=True)
