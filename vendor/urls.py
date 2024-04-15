"""
URL configuration for vendor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from user_details import views as new_app

urlpatterns = [

    path('admin/', admin.site.urls),
    path('Register',new_app.Register,name='Register'),
    path('Address',new_app.Address,name='Address'),
    path('Contact',new_app.Contact,name='Contact'),
    path('Vendor',new_app.Vendor,name='Vendor'),
    path('Get_Register',new_app.Get_Register,name='Get_Register'),
    path('Get_Address',new_app.Get_Address,name='Get_Address'),
    path('Get_Contact',new_app.Get_Contact,name='Get_Contact'),
    path('Get_Vendor',new_app.Get_Vendor,name='Get_Vendor'),
    path('Get_ind_val/<pk>', new_app.Get_ind_val, name='Get_ind_val'),
    path('Get_Address_ind/<pk>', new_app.Get_Address_ind, name='Get_Address_ind'),
    path('Get_Contact_ind/<pk>',new_app.Get_Contact_ind,name='Get_Contact_ind'),
    path('Get_Vendor_ind/<pk>',new_app.Get_Vendor_ind,name='Get_Vendor_ind'),
    path('Index',new_app.Index,name='Index'),
    path('Get_Register_m1',new_app.Get_Register_m1,name='Get_Register_m1'),
    path('Get_Address_m1',new_app.Get_Address_m1,name='Get_Address_m1'),
    path('Get_Contact_m1',new_app.Get_Contact_m1,name='Get_Contact_m1'),
    path('Get_Vendor_m1',new_app.Get_Vendor_m1,name='Get_Vendor_m1'),
    path('Del_Register/<pk>',new_app.Del_Register,name='Del_Register'),
    path('Del_Address/<pk>',new_app.Del_Address,name='Del_Address'),
    path('Del_Contact/<pk>',new_app.Del_Contact,name='Del_Contact'),
    path('Del_Vendor/<pk>',new_app.Del_Vendor,name='Del_Vendor'),
    path('RegLogin',new_app.RegLogin,name='RegLogin')

]


