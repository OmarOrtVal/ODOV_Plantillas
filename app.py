from flask import Flask, render_template, url_for, request, redirect, flash, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'una_clave_secreta_muy_segura_y_larga' 

USERS = [] 


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_email' in session:
        return redirect(url_for('inicio'))
        
    if request.method == 'POST':
        email_login = request.form.get('email_login')
        password_login = request.form.get('password_login')
        
        user_found = None
        for user in USERS:
            if user['email'] == email_login and user['password'] == password_login:
                user_found = user
                break
        
        if user_found:
            session['user_email'] = user_found['email']
            session['user_nombre'] = user_found['nombre']
            flash(f"¡Bienvenido de nuevo, {user_found['nombre']}!", 'success')
            return redirect(url_for('inicio'))
        else:
            flash('Correo electrónico o contraseña incorrectos.', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html', title='Iniciar Sesión', no_menu=True)

@app.route('/logout')
def logout():
    session.pop('user_email', None)
    session.pop('user_nombre', None) 
    flash('Has cerrado sesión exitosamente.', 'info')
    return redirect(url_for('login')) 


@app.route('/')
def index():
    """Ruta raíz: redirige a 'inicio' si está logueado o a 'login' si no lo está."""
    if 'user_email' in session:
        return redirect(url_for('inicio'))
    return redirect(url_for('login')) 

@app.route('/inicio')
def inicio(): 
    """
    Ruta para la página de inicio. Ahora usa session.get('user_nombre') directamente 
    en lugar de g.user_nombre.
    """
    current_user_name = session.get('user_nombre')
    info = f"¡Hola {current_user_name}! Aquí encontrarás información fascinante sobre animales exóticos, vehículos antiguos, maravillas del mundo y más. ¡Explora el menú superior para empezar! (Sesión iniciada como: {session.get('user_email')})"
    
    return render_template('inicio.html', title='Inicio', info=info)


@app.route('/animales-exoticos')
def animales_exoticos():
    """Ruta para la sección de Animales Exóticos."""
    contenido = "Bienvenido a la pestaña dedicada a los animales exóticos. Aquí descubrirás especies únicas de todo el planeta."
    return render_template('animales_exoticos.html', title='Animales Exóticos', content=contenido, user_logged_in=user_logged_in, user_nombre=user_nombre)


@app.route('/vehiculos-antiguos')
def vehiculos_antiguos():
    contenido = "Explora la historia de los automóviles clásicos, su..."
    return render_template('vehiculos_antiguos.html', title='Vehículos Antiguos', content=contenido, user_logged_in=user_logged_in, user_nombre=user_nombre)

@app.route('/maravillas-del_mundo')
def maravillas_del_mundo():
    contenido = "Viaja a través de la historia y admira las siete grandes maravillas del mundo, tanto antiguas como modernas."
    return render_template('maravillas_del_mundo.html', title='Maravillas del Mundo', content=contenido, user_logged_in=user_logged_in, user_nombre=user_nombre)

@app.route('/acerca-de')
def acerca_de(user_logged_in, user_nombre):
    contenido = "Información sobre el desarrollador y el propósito de este sitio web."
    return render_template('acerca_de.html', title='Acerca de...', content=contenido, user_logged_in=user_logged_in, user_nombre=user_nombre)

@app.route('/registrame', methods=['GET', 'POST'])
def registrame():
    if 'user_email' in session:
        return redirect(url_for('inicio'))

    error = None
    if request.method == 'POST':
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
    return redirect(url_for('registrame'))

if __name__ == '__main__':
    app.run(debug=True)
