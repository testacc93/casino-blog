from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('blog/<str:post_name>', views.blog),
    path('contact', views.contact),
]
