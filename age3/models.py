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
        #食べ物
        foodsID = models.CharField(max_length=50)
        foodsName = models.CharField(max_length=50)
        KIND_OF_FOODS = (
                (1,'vgt0'),#野菜・果物
                (2,'met0'),#肉・ハム・ソーセージ
                (3,'fsh0'),#魚介類
                (4,'del0'),#惣菜・お弁当・サラダ
                (5,'egg0'),#卵
                (6,'mlk0'),#牛乳
                (7,'cse0'),#乳製品
                (8,'fmt0'),#発酵食品・練製品
                (9,'ice0'),#冷凍食品・アイス
                (10,'rce0'),#米
                (11,'ndl0'),#麺
                (12,'brd0'),#パン・ジャム・シリアル
                (13,'spc0'),#食油・カレー・スープ・調味料
                (14,'can0'),#缶詰・粉類・乾物
                (15,'swt0'),#菓子・スイーツ
                (16,'dnk0'),#飲料
                (17,'acl0'),#お酒・ノンアルコール
                (18,'pet0'),#ペットフード
                (19,'oth0'),#その他
        )
        foodsKinds = models.IntegerField(
                verbose_name = "種類",
                choices = KIND_OF_FOODS
        )
        foodscreateDate = models.DateTimeField('食べ物登録日時', auto_now_add = True)
        foodsupdateDate = models.DateTimeField('食べ物更新日時', auto_now = True, blank=True, null=True)
        #家電
        electID = models.CharField(max_length=50)
        electName = models.CharField(max_length=50)
        KIND_OF_ELECTRONICS = (
                (1,'wsh1'),#洗濯機
                (2,'vcm1'),#掃除機
                (3,'rck1'),#炊飯器
                (4,'ovn1'),#電子レンジ・オーブントースター
                (5,'iln1'),#アイロン
                (6,'sew1'),#ミシン
                (7,'frg1'),#冷蔵庫
                (8,'pot1'),#ポット・ケトル
                (9,'acd1'),#エアコン
                (10,'fan1'),#扇風機
                (11,'dry1'),#ドライヤー
                (12,'lgt1'),#照明
                (13,'phn1'),#電話機
                (14,'hmd1'),#加湿器・空気清浄機
                (15,'tvs1'),#テレビ
                (16,'cmr1'),#カメラ
                (17,'smp1'),#スマートフォン
                (18,'pcn1'),#パソコン
                (19,'ado1'),#オーディオ
                (20,'toy1'),#おもちゃ
                (21,'gme1'),#ゲーム機
                (22,'oth1'),#その他
        )
        electKinds = models.IntegerField(
                verbose_name = "種類",
                choices = KIND_OF_ELECTRONICS
        )
        electcreateDate = models.DateTimeField('記念日登録日時', auto_now_add = True)
        electupdateDate = models.DateTimeField('記念日更新日時', auto_now = True, blank=True, null=True)
        #記念日
        annivID = models.CharField(max_length=50)
        annivName = models.CharField(max_length=50)
        annivcreateDate = models.DateTimeField('記念日登録日時', auto_now_add = True)
        annivupdateDate = models.DateTimeField('記念日更新日時', auto_now = True, blank=True, null=True)
