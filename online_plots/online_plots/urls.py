"""online_plots URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app import views
from online_plots import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name='login'),
    path('check/',views.check,name='check'),
    path('about/',views.about,name='about'),
    path('index/',views.index,name='index'),
    path('newplot/',views.newplot,name='newplot'),
    path('editplot/', views.editplot, name='editplot'),
    path('viewplot/', views.viewplot, name='viewplot'),
    path('newapp/', views.newapp, name='newapp'),
    path('editapp/',views.editapp,name='editapp'),
    path('viewapp/', views.viewapp, name='viewapp'),
    path('sales/',views.sales,name='sales'),
    path('payments/',views.payments,name='payments'),
    path('reports/',views.reports,name='reports'),
    path('addemp/', views.addemp, name='addemp'),
    path('viewemp/', views.viewemp, name='viewemp'),
    path('soldplots/', views.soldplots, name='soldplots'),
    path('resplots/', views.resplots, name='resplots'),
    path('vacantplots/', views.vacantplots, name='vacantplots'),
    path('saveplot/',views.saveplot,name='saveplot'),
    path('saveapp/',views.saveapp,name='saveapp'),
    path('saveemp/',views.saveemp,name='saveemp'),
    path('delplot/',views.delplot,name='delplot'),
    path('delemp/',views.delemp,name='delemp'),
    path('delapp',views.delapp,name='delapp')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)