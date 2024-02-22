from django.shortcuts import render
from django.http import HttpResponse
from grando.models import Cursos , Alumnos, Profesores
from grando.forms import CursoFormulario , AlumnoFormulario


def index(request):
    return render(request,"index.html")

def cursos(request):
    cursos = Cursos.objects.all()
    return render(request, "cursos.html", {'cursos': cursos})

def alumnos(request):
    alumnos = Alumnos.objects.all()
    return render(request, "alumnos.html", {'alumnos': alumnos})



def profesores(request):
    profesores = Profesores.objects.all()
    return render(request, "profesores.html", {'profesores': profesores})

#def alumnonuevo(request):
    alumnonuevo = Alumnos.objects.all()
    return render(request, "alumnonuevo.html", {'alumnonuevo': alumnonuevo})





#def formulario(request):

    print(request)
    if request.method == 'POST':
    
            curso =  Cursos(request.POST['curso'],(request.POST['camada']))

            curso.save()

            return render(request,"index.html")

    return render(request,"formulario.html")


def formulario(request):
    if request.method == 'POST':
        form = CursoFormulario(request.POST)
        if form.is_valid():
            curso = form.save()  # Esto guarda el curso en la base de datos
            return render(request,'index.html')  
        else:
            # Manejar el caso en que el formulario no sea válido
            # Por ejemplo, podrías renderizar el formulario nuevamente con los errores
            return render(request, 'cursonuevo.html', {'form': form})
    else:
        form = CursoFormulario()
    return render(request, 'cursonuevo.html', {'form': form})

def alumnonuevo(request):
    if request.method == 'POST':
        form = AlumnoFormulario(request.POST)
        if form.is_valid():
            alumno = form.save()  # Esto guarda el curso en la base de datos
            return render(request,'alumnonuevo.html')  
       
    else:
        form = AlumnoFormulario()
    return render(request, 'alumnonuevo.html', {'form': form})


def profesornuevo(request):
    
    if request.method == 'POST':
        form = AlumnoFormulario(request.POST)
        if form.is_valid():
            alumno = form.save()  # Esto guarda el curso en la base de datos
            return render(request,'profesornuevo.html')  
       
    else:
        form = AlumnoFormulario()
    return render(request, 'profesornuevo.html', {'form': form})




def busqueda(request):
    return render(request,"busqueda.html")


def buscar(request):
    if 'camada' in request.GET:
        camada = request.GET['camada']
        cursos = Cursos.objects.filter(camada__icontains=camada)
        return render(request, "busqueda.html", {"cursos": cursos, "camada": camada})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)