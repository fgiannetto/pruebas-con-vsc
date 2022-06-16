from django.shortcuts import render, HttpResponse

# Create your views here.

layout = """
<h1>Sitio web con Django</h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/nosotros">Nosotros</a>
    </li>
    <li>
        <a href="/pagina-pruebas">Página de pruebas</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola Mundo</a>
    </li>
</ul>
"""


def hola_mundo(request):
    return HttpResponse(layout+"""
    <h1>HOLA perrito</h1>
    <h3> Todo bien? </h3>
    """)

def index (request):
    return HttpResponse(layout+request, 'mainapp/index.html',{
        'title': 'INICIO'
    })

def about (request):

    return render(layout+request, 'mainapp/about.html',{
        'title' : 'Sobre Nosotros'
    })

def pagina (request):
    return render(layout+request, 'mainapp/pagina.html',{
        'title' : 'Pagina'
    })