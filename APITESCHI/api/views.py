from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm #Es para los formularios, que tiene django
from django.contrib.auth.forms import AuthenticationForm # Comprobar si el Usuario existe
from django.contrib.auth.models import User #Registrar usuarios en django
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from django.db import IntegrityError
from django.core.mail import EmailMessage





from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags



# Create your views here.
def codigoXML(request):
    return render(request,'codigoXML.html')




#Creacion del Signup
def home(request):
    return render(request,'home.html')

def signup(request):
    
    if request.method == 'GET':
        
         return render(request,'signup.html',{
        'form': UserCreationForm
            })
         
    else:
        
        if request.POST['password1'] == request.POST['password2']:
            try:
                
                user =  User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                
                
                subject = 'correo de registro de usuario'
                mesage = 'agracias por registrarte'
                from_email = 'CarlosBolañosCastro@gmail.com'
                recipient_list = ['ci70232@gmail.com']
                send_mail(subject, mesage, from_email, recipient_list)
                
                
                
                
                return redirect('plantilla')
            
            
            #ENVIO DEL CORREO ELECTRONICO
                
                
               
            
            except:
                
                return render(request,'signup.html',{
                    'form': UserCreationForm,
                    "error": 'usuaio ya existe'
                })
                
        return render(request,'signup.html', {
            'form': UserCreationForm,
            "error": 'Las contraseñas no son iguales'
              })
   
#Creacion de la plantilla cuando se registren.          
def plantilla(request):
    return render(request, 'plantilla.html')
                
#Creacion de login
def signin(request):
    if request.method == 'GET':
        
      return render(request, 'signin.html',{
          'form': AuthenticationForm
      })
    
    else:

        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html',{
          'form': AuthenticationForm,
          'error': 'El usuario o la contraseña son incorrectos'
            })  
        else:
            login(request, user)
            return redirect('plantilla')
              
            
        
  
  
            
            
       
        
    
    
    
    
   
