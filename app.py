from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Ruta de inicio. Muestra la página de login."""
    return render_template('login.html', title='Iniciar Sesión', no_menu=True)

@app.route('/inicio')
def inicio():
    """Ruta para la página de inicio (después de iniciar sesión)."""
    info = "Aquí encontrarás información fascinante sobre animales exóticos, vehículos antiguos, maravillas del mundo y más. ¡Explora el menú superior para empezar!"
    return render_template('inicio.html', title='Inicio', info=info)


@app.route('/animales-exoticos')
def animales_exoticos():
    """Ruta para la sección de Animales Exóticos."""
    contenido = "Bienvenido a la pestaña dedicada a los animales exóticos."
    return render_template('animales_exoticos.html', title='Animales Exóticos', content=contenido)

@app.route('/vehiculos-antiguos')
def vehiculos_antiguos():
    """Ruta para la sección de Vehículos Antiguos."""
    contenido = "Explora la historia de los automóviles clásicos, su diseño atemporal y las leyendas detrás de ellos."
    return render_template('vehiculos_antiguos.html', title='Vehículos Antiguos', content=contenido)

@app.route('/maravillas-del-mundo')
def maravillas_del_mundo():
    """Ruta para la sección de Maravillas del Mundo."""
    contenido = "Descubre las estructuras y sitios naturales más impresionantes creados por la humanidad o por la naturaleza."
    return render_template('maravillas_del_mundo.html', title='Maravillas del Mundo', content=contenido)

@app.route('/acerca-de')
def acerca_de():
    """Ruta para la sección 'Acerca de...'."""
    contenido = "En esta pagina conoceras acerca de el creador de esta pagina web..."
    return render_template('acerca_de.html', title='Acerca de...', content=contenido)

@app.route('/login')
def login():
    """Ruta para la página de Inicio de Sesión."""
    return render_template('login.html', title='Iniciar Sesión', no_menu=True)

@app.route('/registro')
def registro():
    """Ruta para la página de Registro."""
    return render_template('registro.html', title='Registro', no_menu=True)

if __name__ == '__main__':
    app.run(debug=True)
