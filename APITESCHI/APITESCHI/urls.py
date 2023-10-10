"""APITESCHI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from api import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    
    path('admin/', admin.site.urls), #No quitar, sino no servira restablecer la contraseña
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('plantilla/', views.plantilla, name='plantilla'),
    path('signin/', views.signin, name='signin'),
    path('Correo/', views.Correo, name='Correo'),
    
    path('brand/', views.brand, name='brand'),
    path('lookbook/', views.lookbook, name='lookbook'),
    path('producto/', views.producto, name='producto'),
    
    
    
    #Aqui empieza el codigo para restablecer la contraseña
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="Correo_Recuperacion/password_reset_form.html"), name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name="Correo_Recuperacion/password_reset_done.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="Correo_Recuperacion/password_reset_confirm.html"), name='password_reset_confirm'),                                                                       
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="Correo_Recuperacion/password_reset_complete.html"),name='password_reset_complete'),
    #Aqui termina el codigo para restablecer la contraseña
    
    
   

    
]

