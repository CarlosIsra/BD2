from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm #Es para los formularios, que tiene django
from django.contrib.auth.forms import AuthenticationForm # Comprobar si el Usuario existe
from django.contrib.auth.models import User #Registrar usuarios en django
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

#Enviar un correo
from django.core.mail import send_mail
from django.db import IntegrityError
from django.core.mail import EmailMessage
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
                
                user =  User.objects.create_user( last_name=request.POST['last_name'], first_name=request.POST['first_name']
                                                 ,username=request.POST['username'],email=request.POST['email']
                                                 ,password=request.POST['password1'])
                user.save()
                login(request, user)
                
                
               
               
                
                
                
                #ENVIO DEL CORREO ELECTRONICO
                
                # Genera las credenciales de acceso (esto es un ejemplo, debes generar las credenciales de manera adecuada).
                usuario = request.POST['username']
                contraseña = request.POST['password1']

                    # Contenido HTML para el correo
                html_message = render_to_string('bienvenida.html', {'usuario': usuario, 'contraseña': contraseña})
                    # Crea un mensaje de texto plano para el correo (opcional)
                plain_message = strip_tags(html_message)

                    # Asunto del correo
                subject = '¡Bienvenido a nuestra aplicación!'

                    # Dirección de correo remitente
                from_email = 'CarlosBolañosCastro@gmail.com'

                    # Lista de destinatarios
                recipient_list = ['ci70232@gmail.com']

                    # Envía el correo
                send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)

                    
            
                
                return redirect('plantilla')
            
            
          
                
                
               
            
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
              
            
        
  ##ENVIO DE EL CORREO ELECTRONICO
  




def bienvenida(request):
    return render(request,'bienvenida.html')
  
            
            
       
        
    
    
    
    
   
