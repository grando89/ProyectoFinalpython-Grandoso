from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from grando.models import Bebida_blanca ,Vinos, Bebida_sa
from grando.forms import Bebida_Blanca_Formulario , VinoFormulario ,Bebida_Sa_Formulario
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import redirect




def index(request):
    return render(request,"index.html")

def bebida_blanca(request):
    bebida_blanca = bebida_blanca.objects.all()
    return render(request, "bebida_blanca.html", {'bebida_blanca': bebida_blanca})
@login_required
def vinos(request):
    vino = Vinos.objects.all()
    return render(request, "vinos.html", {'vinos': vino})

def bebidas_sa(request):
    bebida_sa = bebida_sa.objects.all()
    return render(request, "bebida_sa.html", {'bebidas_sa': bebida_sa})


@login_required
def formulario(request):
    if request.method == 'POST':
        form = Bebida_Blanca_Formulario(request.POST)
        if form.is_valid():
            bebida_blanca = form.save()  
            return render(request,'index.html')  
        else:
           
            return render(request, 'bebida_blanca.html', {'form': form})
    else:
        form = Bebida_Blanca_Formulario()
    return render(request, 'bebida_blanca.html', {'form': form})
@login_required
def vino_nuevo(request):
    if request.method == 'POST':
        form = VinoFormulario(request.POST)
        if form.is_valid():
            vino = form.save()  # Esto guarda el curso en la base de datos
            return render(request,'index.html')  
       
    else:
        form = VinoFormulario()
    return render(request, 'vinos.html', {'form': form})

@login_required
def bebida_sa_nueva(request):
    
    if request.method == 'POST':
        form = Bebida_Sa_Formulario(request.POST)
        if form.is_valid():
            bebida_sa = form.save()  # Esto guarda el curso en la base de datos
            return render(request,'index.html')  
    else:
        form = Bebida_Sa_Formulario()
    return render(request, 'bebida_sa.html', {'form': form})




def busqueda(request):
    return render(request,"busqueda.html")


#def buscar(request):
    
    
    
    if request.method == 'GET':
        nombre_curso = request.GET.get('nombre_curso', '')
        nombre_alumno = request.GET.get('nombre_alumno', '')
        nombre_profesor = request.GET.get('nombre_profesor', '')
        
        # Filtros
        filtros = {}
        if nombre_curso:
            filtros['nombre__icontains'] = nombre_curso
        if nombre_alumno:
            filtros['nombre__icontains'] = nombre_alumno
        if nombre_profesor:
            filtros['nombre__icontains'] = nombre_profesor
        
        cursos = Cursos.objects.filter(**filtros)
        alumnos = Alumnos.objects.filter(**filtros)
        profesores = Profesores.objects.filter(**filtros)
        
        return render(request, "busqueda.html", {"cursos": cursos, "alumnos": alumnos, "profesores": profesores})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)
    


#def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contrasenia = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contrasenia)


            if user is not None:
                login(request,user)
                return render (request ,"index.html" , {"mensaje":f"Bienvenido {usuario}"})
            
            else:
                return render(request,"login.html" , {"mensaje":"Error, datos incorrectos"})
            
        else:
                return render(request,"login.html", {"mensaje":"Error, formulario erroneo"}) 

    form= AuthenticationForm()
    return render(request,"login.html" , {"form": form})
@login_required
def agregados(request):
    bebida_blanca = Bebida_blanca.objects.all()
    vino = Vinos.objects.all()
    bebida_sa = Bebida_sa.objects.all()

    return render(request, "pedido.html", {'bebida_blanca': bebida_blanca, 'vino': vino, 'bebida_sa': bebida_sa})



def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request,"index.html" , {"mensaje":"Usuario Creado "})
        

        else:
            form = UserCreationForm()


        return render(request,"registro.html",{"form": form})    
    



def buscar_vinos(request):
    if 'query' in request.GET:
        query = request.GET['query']
        resultados = buscar_vinos_en_lista(query)
    else:
        resultados = None
    return render(request, 'busqueda.html', {'resultados': resultados, 'query': query})

def buscar_vinos_en_lista(query):
    vinos = {
        'Cabernet Sauvignon': [
            'Caymus Vineyards Cabernet Sauvignon',
            'Silver Oak Alexander Valley Cabernet Sauvignon',
            'Joseph Phelps Insignia',
            'Stag\'s Leap Wine Cellars Artemis Cabernet Sauvignon',
            'Opus One',
            'Jordan Alexander Valley Cabernet Sauvignon',
            'Shafer Vineyards Hillside Select',
            'Ridge Monte Bello',
            'Heitz Cellar Martha\'s Vineyard Cabernet Sauvignon',
            'Dominus Estate'
        ],
        'Merlot': [
            'Duckhorn Vineyards Three Palms Vineyard Merlot',
            'Shafer Vineyards Merlot',
            'Pride Mountain Vineyards Merlot',
            'Twomey Merlot by Silver Oak',
            'Leonetti Cellar Merlot',
            'Paloma Merlot',
            'Langtry Estate Centennial Reserve Merlot',
            'Chateau Petrus',
            'Rombauer Vineyards Merlot',
            'Janzen Estate Cloudy\'s Vineyard Merlot'
        ],
        'Chardonnay': [
            'Chateau Montelena Chardonnay',
            'Kistler Vineyards Chardonnay',
            'Peter Michael Winery Belle Cote Chardonnay',
            'Shafer Red Shoulder Ranch Chardonnay',
            'Far Niente Chardonnay',
            'Ramey Wine Cellars Ritchie Vineyard Chardonnay',
            'Aubert Chardonnay',
            'Marcassin Vineyard Chardonnay',
            'Kongsgaard Chardonnay',
            'Sonoma-Cutrer Russian River Ranches Chardonnay'
        ],
        'Syrah': [
            'Alban Vineyards Reva Alban Estate Syrah',
            'Sine Qua Non Syrah',
            'Pax Syrah',
            'Andrew Murray Vineyards Tous les Jours Syrah',
            'Qupé Syrah',
            'Penfolds Grange Shiraz',
            'E. Guigal Côte-Rôtie La Mouline',
            'Clape Cornas',
            'Cayuse Vineyards Bionic Frog Syrah',
            'Jean-Luc Colombo Les Terres Brûlées Cornas Syrah'
        ]
    }

    resultados = {}
    for tipo, lista_vinos in vinos.items():
        resultados[tipo] = [vino for vino in lista_vinos if query.lower() in vino.lower()]

    return resultados




def buscar_bebidas_blancas(request):
    if 'query' in request.GET:
        query = request.GET['query']
        resultados = buscar_bebidas_blancas_en_lista(query)
    else:
        resultados = None
    return render(request, 'busqueda.html', {'resultados': resultados, 'query': query})

def buscar_bebidas_blancas_en_lista(query):
    bebidas_blancas = {
        'Vodka': [
            'Absolut Vodka',
            'Grey Goose Vodka',
            'Belvedere Vodka',
            'Ketel One Vodka',
            'Stolichnaya Vodka',
            'Tito\'s Handmade Vodka',
            'Smirnoff Vodka',
            'Finlandia Vodka',
            'Skyy Vodka',
            'Chopin Vodka'
        ],
'Whisky': [
    'Jack Daniel\'s Tennessee Whiskey Whisky',
    'Johnnie Walker Black Label Whisky',
    'Jameson Irish Whiskey Whisky',
    'Macallan 12 Year Old Whisky',
    'Glenlivet 12 Year Old Whisky',
    'Bulleit Bourbon Whisky',
    'Buffalo Trace Whisky',
    'Laphroaig 10 Year Old Whisky',
    'Woodford Reserve Whisky',
    'Maker\'s Mark Bourbon Whisky'
],
        'Gin': [
            'Tanqueray Gin',
            'Bombay Sapphire Gin',
            'Hendrick\'s Gin',
            'Beefeater Gin',
            'Gordon\'s Gin',
            'Plymouth Gin',
            'Broker\'s Gin',
            'No. 209 Gin',
            'Monkey 47 Gin',
            'Aviation Gin'
        ]
    }

    resultados = {}
    for tipo, lista_bebidas in bebidas_blancas.items():
        resultados[tipo] = [bebida for bebida in lista_bebidas if query.lower() in bebida.lower()]

    return resultados



def buscar_bebidas_sin_alcohol(request):
    if 'query' in request.GET:
        query = request.GET['query']
        resultados = buscar_bebidas_sin_alcohol_en_lista(query)
    else:
        resultados = None
    return render(request, 'busqueda.html', {'resultados': resultados, 'query': query})

def buscar_bebidas_sin_alcohol_en_lista(query):
    bebidas_sin_alcohol = {
        'Refrescos y Aguas': [
            'Coca-Cola',
            'Pepsi',
            'Sprite',
            'Fanta',
            '7-Up',
            'Mountain Dew',
            'Mirinda',
            'Limonada',
            'Tónica',
            'Agua Mineral'
        ],
        'Jugos y Néctares': [
            'Jugo de Naranja',
            'Jugo de Manzana',
            'Jugo de Piña',
            'Jugo de Uva',
            'Jugo de Mango',
            'Jugo de Guayaba',
            'Néctar de Durazno',
            'Néctar de Ciruela',
            'Néctar de Pera',
            'Néctar de Maracuyá'
        ],
        'Bebidas Sin Alcohol Especiales': [
            'Sidra sin Alcohol',
            'Cerveza sin Alcohol',
            'Vino sin Alcohol',
            'Cócteles Sin Alcohol',
            'Bebidas Energéticas Sin Alcohol',
            'Té Helado sin Alcohol',
            'Café Descafeinado',
            'Smoothies',
            'Malta sin Alcohol',
            'Horchata'
        ]
    }

    resultados = {}
    for tipo, lista_bebidas in bebidas_sin_alcohol.items():
        resultados[tipo] = [bebida for bebida in lista_bebidas if query.lower() in bebida.lower()]

    return resultados



def eliminar_vino(request):
    if request.method == 'POST':
        vino_id = request.POST.get('vino_id')
        Vinos.objects.filter(id=vino_id).delete()
    return redirect('pedido')


def eliminar_bebida_blanca(request):
    if request.method == 'POST':
        bebida_blanca_id = request.POST.get('bebida_blanca_id')
        Bebida_blanca.objects.filter(id=bebida_blanca_id).delete()
    return redirect('pedido')

def eliminar_bebida_sa(request):
    if request.method == 'POST':
        bebida_sa_id = request.POST.get('bebida_sa_id')
        Bebida_sa.objects.filter(id=bebida_sa_id).delete()
    return redirect('pedido')