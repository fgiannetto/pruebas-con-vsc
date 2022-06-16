from flask import Flask

app = Flask (__name__)

@app.route('/')
def index():
    return "Aprendiendo Flask" 

@app.route('/info')
def info():
    return "<h1>Pestaña de Información</h1>"

@app.route('/contacto')
def contacto():
    return "<h1>Pestaña de contactos</h1>"

@app.route('/lenguajes')
def lenguajes():
    return "<h1>Pestaña de lenguajes</h1>"


if __name__ =='__main__':
    app.run(debug=True)

