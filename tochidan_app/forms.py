from django import forms
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.core.mail import EmailMessage
from .models import TochidanApp


class ContactForm(forms.Form):
    name = forms.CharField(label='', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': "お名前"}),
                           )
    email = forms.EmailField(label='',
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': "メールアドレス", }),
                             )
    message = forms.CharField(label='',
                              widget=forms.Textarea(attrs={'class': 'form-control',
                                                           'placeholder': "お問い合わせ内容", }),
                              )

    def send_email(self):
        subject = "お問い合わせ"
        message = self.cleaned_data['message']
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        from_email = '{name} <{email}>'.format(name=name, email=email)
        recipient_list = [settings.EMAIL_HOST_USER]  # 受信者リスト
        try:
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")

        subject = 'お問い合わせ{}'.format(subject)
        message = '送信者名: {0}\nメールアドレス: {1}\nメッセージ:\{2}'.format(name, email, message)
        from_email = 'admin@example.com'
        to_list = [
            'test@example.com'
        ]
        cc_list = [
            email
        ]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
        message.send()


class TochidanCreateForm(forms.ModelForm):
    number_of_people = forms.ChoiceField(choices=[(num, num) for num in range(1, 101)])
    number_of_people.label = "構成人数"

    start = forms.ChoiceField(
        choices=(
            ("", ""),
            ('音先', '音先'),
            ('板先', '板先'),
        )
    )
    start.label = "ダンス開始きっかけ"

    activity_histori = forms.ChoiceField(
        choices=(
            ("", ""),
            ('3ヶ月未満', '3ヶ月未満'),
            ('3ヶ月〜6ヶ月', '3ヶ月〜6ヶ月'),
            ('6ヶ月〜1年', '6ヶ月〜1年'),
            ('1年以上', '1年以上'),
        )
    )
    activity_histori.label = "活動歴"

    class Meta:
        model = TochidanApp
        fields = (
            'team_name',
            'yomigana',
            'photo',
            'audio',
            'start',
            'number_of_people',
            'genre',
            'representative',
            'telephone_number',
            'email',
            'school_name',
            'activity_histori',
            'comment',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
