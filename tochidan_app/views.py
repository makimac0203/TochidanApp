import logging

from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView

from django.views.generic.edit import FormView
from .forms import ContactForm, TochidanCreateForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import TochidanApp
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin

logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "index.html"


class ContactView(generic.FormView):
    template_name = "contact/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('tochidan_app:contact_result')

    def form_valid(self, form):
        form.send_email()
        logger.info('Contact sent by{}'.format(form.cleaned_data['name']))
        return super().form_valid(form)


class ContactResultView(TemplateView):
    template_name = 'contact/contact_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "お問い合わせは正常に送信されました。"
        return context



class TochidanUserDetailView(UserPassesTestMixin, LoginRequiredMixin, generic.DetailView):
    model = TochidanApp
    template_name = 'tochidan_user_detail.html'
    pk_url_kwarg = 'pk'
    # UserPassesTestMixinのtest_funkによりsuperuser意外をURLのidを変えて他のユーザーページへの閲覧を防止する
    def test_func(self):
        # pkが現在ログイン中ユーザと同じ、またはsuperuserならOK。
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class TochidanUserCreateView(LoginRequiredMixin, generic.CreateView):
    model = TochidanApp
    template_name = 'tochidan_user_create.html'
    form_class = TochidanCreateForm

    # ユーザーの詳細情報を登録すると、ユーザーページに遷移する。
    def get_success_url(self):
        return reverse("tochidan_app:tochidan_user_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        tochidan_app = form.save(commit=False)
        tochidan_app.user = self.request.user
        tochidan_app.save()
        messages.success(self.request, 'チーム情報を登録しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "登録に失敗しました。")
        return super().form_invalid(form)


class TochidanUserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TochidanApp
    template_name = 'tochidan_user_update.html'
    form_class = TochidanCreateForm

    def get_success_url(self):
        return reverse_lazy('tochidan_app:tochidan_user_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, 'チーム情報を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "更新に失敗しました。")
        return super().form_invalid(form)


class SuperUserOnlyView(SuperuserRequiredMixin, ListView):
    model = TochidanApp
    template_name = 'tochidan_user_list.html'

    def get_queryset(self):
        tochidan_apps = TochidanApp.objects.order_by('-created_at')
        return tochidan_apps
