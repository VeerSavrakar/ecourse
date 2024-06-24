from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name='s_app'
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='s_app/login.html'),name='logi'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/',views.CreateForm.as_view(),name='signup'),
]
