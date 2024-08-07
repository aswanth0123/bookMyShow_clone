from django.urls import path
from .import views

urlpatterns=[
    path('login',views.login),
    path('logout',views.logout1),
    path('',views.index),
    path("see_all/<lang>",views.see_all),
    path("see_all",views.see_all),
    path("movie/<name>",views.view_movie),
    path('register',views.register),
    path('view_theatre/<name>',views.view_theatre),
]