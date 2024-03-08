from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.http import HttpResponse


# Create your views here.
def login_request(request):
    msg_login =""
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contrasenia = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contrasenia)


            if user is not None:
                login(request,user)
                return render (request ,"index.html" , {"mensaje":f"Bienvenido {usuario}"})
            
        msg_login = "Usuario o contraseña Incorrectas"    

    form= AuthenticationForm()
    return render(request,"login.html" , {"form": form})




def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "index.html", {"mensaje": "Usuario Creado "})

    return render(request, "register.html", {"form": form})