from django.db import models
from django.utils import timezone

class User(models.Model):
        userID = models.CharField(max_length=200)
        userName = models.CharField(max_length=200)
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

