
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reg, name='Home-Page'),
    path('reg', views.reg_verification, name="reg_verification"),
    path('verify', views.verify, name="verify"),
]
