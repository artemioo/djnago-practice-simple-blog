from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', main_view, name='main_url'),
    path('post/<str:slug>/', post_view, name='post_detail_url')
]
