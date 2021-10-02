

from accounts.models import CustomUser
from django.conf import settings
from django.db import models


class TochidanApp(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    team_name = models.CharField(verbose_name='チーム名', max_length=40)
    photo = models.ImageField(verbose_name='チーム写真', blank=True, null=True)
    record = models.FileField(verbose_name='使用曲', upload_to='documents/', blank=True, null=True)
    number_of_people = models.IntegerField(verbose_name='構成人数', blank=True, null=True, default=0)
    created_at = models.DateTimeField(verbose_name='登録日時s', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'TochidanApp'
        

    def __str__(self):
        return self.team_name
