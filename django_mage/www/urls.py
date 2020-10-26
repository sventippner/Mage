"""www URL Configuration

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

from django_mage.mage_admin.views import bot_index, del_sdc, sdc_build #, sdc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bot_index),
#    path('sdc/', sdc),
    path('sdc/d/<str:name>/', del_sdc, name="del_sdc"),
    path('sdc/build/', sdc_build, name="sdc_build")
]
