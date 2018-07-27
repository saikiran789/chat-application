from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import login, logout
from chat.views import index
from chat.views import userlist
from django.conf.urls import include,url

urlpatterns = [
    path('', index),
    path('accounts/login/', login),
    path('accounts/logout/', logout),
    path('admin/', admin.site.urls),
    path('userlist/', userlist),
]
