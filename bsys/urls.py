"""bus_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views

app_name = 'bsys'
urlpatterns = [
    path("",views.index,name ='index'),
    path("home/",views.home,name ='home'),
    path('profile/b/delete/<int:pk>', views.BusDeleteView.as_view(), name='BusDelete'),
    path('profile/d/delete/<int:pk>', views.DriverDeleteView.as_view(), name='DriverDelete'),
    # path("signup/",views.sign_up,name ='signup'),
    path('profile/b/list/', views.BusList.as_view(), name='BusList'),
    path('profile/d/list/', views.DriverList.as_view(), name='DriverList'),
    path('signup/', views.DriverSignUpView.as_view(), name='signup'),
    path("success/",views.success_test,name ='success'),
    path("faliur/",views.faliur_test,name ='faliur'),
    path("logout/",views.logout_view,name="logout"),
    path("profile/",views.profile,name="profile"),
    path('profile/d/create/', views.DriverSignUpFormView.as_view(), name='driverCreate'),
    path('profile/b/create/', views.BusCreationFormView, name='BusCreate'),
    path('profile/b/update/', views.BusUpdateView, name='BusUpdate'),
]
