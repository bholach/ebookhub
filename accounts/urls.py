from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from . import views
# from django.contrib.auth.views import login
# from django.contrib.auth.views import logout

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.about, name='contact'),
    # path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout', views.userLogout, name='logout'),
    path('register_success', views.register_success, name='register_success'),
]
# url(r'^logout/$', auth_views.logout, name='logout'),
# url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
