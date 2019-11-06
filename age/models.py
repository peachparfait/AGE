from django.db import models
from django.utils import timezone

class User(models.Model):
    userName = models.CharField(max_length=20)
    mailAddless = models.EmailField(max_length=50)
    #passWord = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    #TEL = models.PositiveIntegerField(max_length=11)
    birthday = models.DateField(max_length=8)
    REVIEW_STAR_CHOICES = (
	    (1,'1'),
	    (2,'2'),
	    (3,'3'),
	    (4,'4'),
	    (5,'5'),
    )

    review_star = models.IntegerField(
        verbose_name="レビュー星",
        choices=REVIEW_STAR_CHOICES)

    GENDER_CHOICES = (
	    (1,'男性'),
	    (2,'女性'),
	    (3,'その他'),
    )
    gender = models.IntegerField(
        verbose_name="性別",
        choices=GENDER_CHOICES)

    reviewComment = models.TextField()
    createDate =  models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(auto_now = True)
#次回までに他のフィールドのクラスも作っておく！
