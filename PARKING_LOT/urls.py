"""PARKING_LOT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url #URLconf is a set of patterns that Django will try to match the requested URL to find the correct view.
from PARK.api import UserList,UserDetail
#path vs url :path() always matches the complete path, so path('account/login/') is equivalent to url('^account/login/$')
#path does not uses regex while url uses regex
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/users_list/$', UserList.as_view(),name='user_list'),

    url(r'^api/users_list/(?P<number>\d+)/$', UserDetail.as_view(), name='user_list'),
    #url(r'^api/users_list/(?P<car_number>\d+)/$', UserDetail.as_view(), name='user_list')
]