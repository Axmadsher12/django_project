"""djangofile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from mpfiles.views import Update_table,Delete_table,Add_table,Table

urlpatterns = [
    path('admin/', admin.site.urls),

    path('Update_table/<id>/',Update_table,name='Update_table'),
    path('Add_table/',Add_table,name='Add_table'),
    path('Delete_table/<id>/',Delete_table,name='Delete_table'),
    path('',Table,name="Tables"),
]
