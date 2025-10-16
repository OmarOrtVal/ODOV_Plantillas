from flask import Flask, render_template, url_for, request, redirect, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'una_clave_secreta_muy_segura_y_larga' 

@app.route('/')
def index():
    """Ruta de inicio. Redirige a login."""
    return redirect(url_for('login')) 

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Ruta para la página de Inicio de Sesión."""
    if request.method == 'POST':
        email = request.form.get('email_login')
        password = request.form.get('password_login')

        if email == "test@correo.com" and password == "1234":
            flash('¡Bienvenido! Has iniciado sesión correctamente.', 'success')
            return redirect(url_for('inicio'))
        else:
            flash('Fallo al iniciar sesión. Verifica tu correo y contraseña.', 'danger')

    return render_template('login.html', title='Iniciar Sesión')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    """Ruta para la página de Registro."""
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        email = request.form.get('email_registro') 
        
        if not all([nombre, apellido, email]):
            flash('Todos los campos son obligatorios.', 'danger')
            return render_template('registro.html', title='Registro')

        print(f"Nuevo usuario registrado: {nombre} {apellido} con correo {email}")
        
        flash('Registro exitoso. ¡Ahora puedes iniciar sesión!', 'success')
        return redirect(url_for('login'))
        
    return render_template('registro.html', title='Registro')

if __name__ == '__main__':
    app.run(debug=True)
