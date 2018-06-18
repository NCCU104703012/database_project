"""nccu_database_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from main_search import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^search/$', views.search_Commodity),
    re_path(r'^search_Record/$', views.search_Record),
    re_path(r'^add_user/$', views.add_user),
    re_path(r'^set_user/$', views.set_user),
    re_path(r'^add_commodity/$', views.add_commodity),
    re_path(r'^set_commodity/$', views.set_commodity),
    re_path(r'^buy_commodity/$', views.buy_commodity),
    re_path(r'^set_record/$', views.set_record),
]
