
from phonenumber_field.modelfields import PhoneNumberField
from embed_video.fields import EmbedVideoField
from accounts.models import CustomUser
from django.conf import settings
from django.db import models


class TochidanApp(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    team_name = models.CharField(verbose_name='チーム名', max_length=40)
    yomigana = models.CharField(verbose_name='チーム読み仮名', max_length=40)
    photo = models.ImageField(verbose_name='チーム写真', upload_to='image/', blank=True, null=True)
    audio = models.FileField(verbose_name='使用曲', upload_to='audio/', blank=True, null=True)
    start = models.CharField('ダンス開始きっかけ', max_length=40, blank=True, null=True)
    number_of_people = models.IntegerField(verbose_name='構成人数', blank=True, null=True,)
    activity_histori = models.CharField('活動歴', max_length=40, blank=True, null=True)
    youtube = EmbedVideoField(verbose_name='ユーチューブ', blank=True, null=True)
    genre = models.CharField(verbose_name='ダンスジャンル', max_length=40, blank=True, null=True)
    school_name = models.CharField(verbose_name='ダンス・スクール名', max_length=40, blank=True, null=True)
    representative = models.CharField(verbose_name='代表者名', max_length=40, blank=True, null=True)
    telephone_number = models.CharField(verbose_name='電話番号', max_length=30, blank=True, null=True)
    email = models.EmailField(verbose_name='メールアドレス', blank=True, null=True)
    comment = models.TextField(verbose_name='コメント・実績・PRなどなど', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='登録日時s', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'TochidanApp'
        

    def __str__(self):
        return self.team_name
