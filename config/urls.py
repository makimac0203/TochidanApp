from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('tochidan_app.urls')),
                  path('accounts/', include('allauth.urls')),
              ]
