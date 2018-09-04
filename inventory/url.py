from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('/accounts/login/', views.login, name='login'),
    path('', views.login, name='login'),
    path('additem', views.additem, name='additem'),
    path('voucherinfo', views.voucherinfo, name='voucherinfo'),
    path('voucherlist', views.voucherlist, name='voucherlist'),
]