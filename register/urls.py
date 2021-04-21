from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.conf.urls import  url

urlpatterns = [
    path('',views.register,name="register"),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('/forgotpassword',views.forgotPassword,name="forgotpassword")
]