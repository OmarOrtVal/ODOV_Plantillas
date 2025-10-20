from flask import Flask, render_template, url_for, request, redirect, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'una_clave_secreta_muy_segura_y_larga' 

USERS = [] 

@app.route('/')
def index():
    """Ruta de inicio. Redirige a login."""
    return redirect(url_for('login')) 

@app.route('/inicio')
def inicio():
    """Ruta para la página de inicio (después de iniciar sesión)."""
    user = {'nombre': 'Explorador'} 
    
    info = f"¡Hola {user['nombre']}! Aquí encontrarás información fascinante sobre animales exóticos, vehículos antiguos, maravillas del mundo y más. ¡Explora el menú superior para empezar!"
    return render_template('inicio.html', title='Inicio', info=info)


@app.route('/animales-exoticos')
def animales_exoticos():
    """Ruta para la sección de Animales Exóticos."""
    contenido = "Bienvenido a la pestaña dedicada a los animales exóticos. Aquí descubrirás especies únicas de todo el planeta."
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
    """Ruta para la página de Inicio de Sesión. Verifica los datos registrados en USERS."""
    
    if request.method == 'POST':
        email = request.form.get('email_login')
        password = request.form.get('password_login')

        user_found = None
        
        for user in USERS:
            if user['email'] == email and user['password'] == password:
                user_found = user
                break

        if user_found:
            flash(f'¡Bienvenido, {user_found["nombre"]}! Has sido validado (pero no recordado).', 'success')
            return redirect(url_for('inicio'))
        else:
            flash('Fallo al iniciar sesión. Verifica tu correo y contraseña.', 'danger')
            return redirect(url_for('registro')) 

    return render_template('login.html', title='Iniciar Sesión', no_menu=True)

@app.route('/registrame', methods=('GET', 'POST')) 
def registrame():
    """Ruta para la página de Registro. Guarda los datos en el objeto USERS."""
    global USERS 
        
    error = None

    if request.method == "POST":
        nombre = request.form.get('nombre') 
        apellido = request.form.get('apellido')
        email = request.form.get('contacto') 
        password = request.form.get('contrasena') 
        confirmPassword = request.form.get('confirmaContraseña') 
        
        if not all([nombre, apellido, email, password, confirmPassword]):
            error = 'Todos los campos son obligatorios.'
        
        if error is None:
            for user in USERS:
                if user['email'] == email:
                    error = f'El correo electrónico "{email}" ya está registrado.'
                    break

        if error is None and password != confirmPassword:
            error = "La contraseña no coincide" 
        
        if error is not None:
            flash(error, 'danger')
            return redirect(url_for('registrame')) 
        else:
            new_user = {
                'nombre': nombre,
                'apellido': apellido,
                'email': email,
                'password': password 
            }
            USERS.append(new_user) 
            flash('¡Registro exitoso! Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('login'))

    return render_template('registro.html', title='Registro', no_menu=True)

@app.route('/registro')
def registro():
    """Ruta de transición para el registro."""
    return redirect(url_for('registrame'))

if __name__ == '__main__':
    app.run(debug=True)
