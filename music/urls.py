from django.conf.urls import url
from django.conf import settings
from .import views
from django.contrib.auth.views import login, logout


urlpatterns = [

    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout/$', logout, {'template_name': 'music/logout.html'}),
    url(r'^register/$', views.register, name="register"),
    url(r'^profile/$', views.view_profile, name="view_profile"),
    url(r'^profile/edit/$', views.edit_profile, name="edit_profile"),
    url(r'^home/$', views.home, name='home'),
]