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
    path('tochidan-user-detail/<int:pk>/', views.TochidanUserDetailView.as_view(), name="tochidan_user_detail"),
    path('tochidan-user-create/', views.TochidanUserCreateView.as_view(), name="tochidan_user_create"),
    path('tochidan-user-update/<int:pk>/', views.TochidanUserUpdateView.as_view(), name="tochidan_user_update"),
    path('tochidan-user-list/', views.TochidanUserListView.as_view(), name="tochidan_user_list"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
