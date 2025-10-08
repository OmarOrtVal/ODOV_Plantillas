from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/inicio')
def inicio():
    """Ruta para la página de inicio."""
    info = "Bienvenido a nuestra página. Aquí encontrarás información fascinante sobre animales exóticos, vehículos antiguos, maravillas del mundo y más. ¡Explora el menú superior para empezar!"
    return render_template('inicio.html', title='Inicio', info=info)

@app.route('/animales-exoticos')
def animales_exoticos():
    """Ruta para la sección de Animales Exóticos."""
    contenido = "Esta sección está dedicada a las especies más raras y fascinantes del planeta. Conoce sus hábitats, características y esfuerzos de conservación."
    return render_template('animales_exoticos.html', title='Animales Exóticos', content=contenido)

@app.route('/vehiculos-antiguos')
def vehiculos_antiguos():
    """Ruta para la sección de Vehículos Antiguos."""
    contenido = "Un viaje al pasado sobre ruedas. Explora la historia de los automóviles clásicos, su diseño atemporal y las leyendas detrás de ellos."
    return render_template('vehiculos_antiguos.html', title='Vehículos Antiguos', content=contenido)

@app.route('/maravillas-del-mundo')
def maravillas_del_mundo():
    """Ruta para la sección de Maravillas del Mundo."""
    contenido = "Descubre las estructuras y sitios naturales más impresionantes creados por la humanidad o por la naturaleza. Desde pirámides hasta formaciones geológicas únicas."
    return render_template('maravillas_del_mundo.html', title='Maravillas del Mundo', content=contenido)

@app.route('/acerca-de')
def acerca_de():
    """Ruta para la sección 'Acerca de...'."""
    contenido = "Somos un equipo de entusiastas dedicados a compartir contenido de alta calidad e interesante sobre temas variados. Nuestro objetivo es educar e inspirar."
    return render_template('acerca_de.html', title='Acerca de...', content=contenido)

if __name__ == '__main__':
    app.run(debug=True)