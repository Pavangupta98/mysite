from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from website3 import views

urlpatterns = [
    url(r'^$', views.login_redirect, name='loin_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls', namespace="music")),
]
