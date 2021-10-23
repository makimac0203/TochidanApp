from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from ..models import TochidanApp


# class LoggedInTestCase(TestCase):
#     """各テストクラスで共通の事前準備処理をオーバーライドした独自TestCaseクラス"""

    # def setUp(self):
    #     """テストメソッド実行前の事前設定"""

        # テストユーザーパスワード
        # self.password = 'hogehoge'

        # 各インスタンスメソッドで使うテスト用ユーザーを生成し
        # インスタンス変数に格納しておく
        # self.test_user = get_user_model().objects.create_user(
        #     username='nrk',
        #     email='nrk36702@nifty.com',
        #     password=self.password)

        # テスト用ユーザーでログインする
        # self.client.login(email=self.test_user.email, password=self.password)


# class TestTochidanUserCreateView(LoggedInTestCase):
#     """TochidanUserCreateView用のテストクラス"""

    # def test_create_user_success(self):
    #     """ダンスチーム情報作成処理が成功するかを検証する"""

        # Postパラメータ
        # params = {''}