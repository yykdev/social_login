
from django.conf.urls import url

from social_login import views

app_name='accounts'
urlpatterns=[
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
]