from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login

def welcome(request):
    # si estamos identificado devolvemos la portada
    if request.user.is_authenticated:
        return render(request, 'users/welcome.html')
    return redirect('/users/login')

def login(request):
    # Creamos un formulario de authenticación vacio
    form = AuthenticationForm()
    if request.user.is_authenticated:
    	return render(request, 'users/welcome.html')
    if request.method == 'POST':
        # Añaimos los datos recibidos al formulario.
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es valido
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Varificamos las credenciales del usuario.
            user = authenticate(username=username, password=password)
            # si existe un usaurio con ese nombre y contraseña
            if user is not None:
                do_login(request, user)
                return redirect('/')
    return render(request, 'users/login.html', {'form' : form})

def logout(request):
    # Finalización de la sesión
    do_logout(request)
    # Regresamos a la pagina de inicio.
    return redirect('users/login')


