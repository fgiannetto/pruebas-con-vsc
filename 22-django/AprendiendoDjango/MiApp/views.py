from django.shortcuts import render, HttpResponse, redirect
from MiApp.models import Article

# Create your views here.

# MVC = Modelo Vista Controlador -> Acciones (metodos)
# MVT = Modelo Template Vista -> Acciones (metodos)

layout = """
<h1> Sitio web con django </h1>
<hr/>
<ul>
    <li>
        <a href="/inicio"> Inicio </a>
    </li>
    <li>
        <a href= "/hola-mundo"> Hola Mundo </a>
    </li>
    <li>
        <a href= "/pagina-pruebas">Pagina de pruebas </a>
    </li>
    <li>
        <a href= "/contacto">Contacto </a>
    </li>
</ul>
<hr/>
"""

def index (request):

    html =  """
        <h1>Inicio</h1>
        <p> años hasta 2050 </p>
        <ul>
    """
    year = 2020
    while year <= 2050:
        if year %2==0:
            html+= f"<li> {str(year )}</li>"

        year +=1

    html += "</ul>"

    nombre = 'Franco Giannetto'
   

    return render (request, 'index.html', {
        'title': 'Inicio',
        'mi_variable':'Soy un dato random',
        'nombre': nombre
    })


def hola_mundo (request):
    return render (request, 'hola_mundo.html')

def pagina (request, redirigir=0):
    if redirigir == 1:
        return redirect('https://google.com')


    return render (request, 'pagina.html')

def contacto (request, nombre="", apellidos=""):
    html=""
    if nombre and apellidos:
        html += "<p>El nombre completo es: </p>"
        html += f"<h3>{nombre} {apellidos}</h3>"

    return HttpResponse(layout+f"<h2>Contacto</h2>"+html)

def crear_articulo(request):
    articulo = Article(
        title = 'Había una vez un arbol',
        content = 'En el medio de La Pampa (que no existe)',
        public = True
    )
    articulo.save()
    
    return HttpResponse(f"Articulo creado: <strong>{articulo.title} - {articulo.content} </strong>")