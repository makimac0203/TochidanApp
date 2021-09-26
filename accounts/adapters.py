from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse_lazy
from tochidan_app.models import TochidanApp
from django.shortcuts import get_object_or_404, render


class MyAccountAdapter(DefaultAccountAdapter):
    # 新規アカウントを登録後、ログインしてからユーザーの詳細情報を登録したか、してないかで遷移先を分岐している
    # model = TochidanApp

    def get_login_redirect_url(self, request):
        user = self.request.user.id
        if TochidanApp.objects.filter(user_id=user).exists():
            path = "/tochidan-user-detail/{pk}/"
            return path.format(pk=self.request.user.id)
        else:
            return reverse_lazy("tochidan_app:tochidan_user_create")
