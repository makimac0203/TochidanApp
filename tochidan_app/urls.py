from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import ContactView, ContactResultView

app_name = 'tochidan_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('contact/result/', ContactResultView.as_view(), name='contact_result'),
    path('tochidan-user/<int:pk>/', views.TochidanUserView.as_view(), name="tochidan_user"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
