from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TochidanApp

class IndexView(generic.TemplateView):
    template_name = "index.html"


class ContactView(FormView):
    template_name = "contact/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('tochidan_app:contact')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        return super().form_valid(form)

class ContactResultView(TemplateView):
    template_name = 'contact/contact_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "お問い合わせは正常に送信されました。"
        return context

class TochidanUserView(LoginRequiredMixin, generic.DetailView):
    model = TochidanApp
    template_name = 'tochidan_user.html'
    pk_url_kwarg = 'pk'

    def get_queryset(self):
        tochidan_apps = TochidanApp.objects.filter(user=self.request.user).order_by('-created_at')
        return tochidan_apps