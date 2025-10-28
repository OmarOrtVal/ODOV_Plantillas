from flask import Flask, render_template, url_for, request, redirect, flash, session

USERS = [
    {
        'nombre': 'Administrador',
        'apellido': 'Sistema',
        'email': 'admin@correo.com',
        'password': 'Admin123'  
    }
]

app = Flask(__name__)
app.config['SECRET_KEY'] = 'una_clave_secreta_muy_segura_y_larga' 

@app.context_processor
def inject_user_data():
    current_user = 'user_email' in session
    user_nombre = session.get('user_nombre', 'Invitado')
    return dict(current_user=current_user, user_nombre=user_nombre)


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
    """Cierra la sesión del usuario."""
    session.pop('user_email', None)
    session.pop('user_nombre', None) 
    flash('Has cerrado sesión exitosamente.', 'info')
    return redirect(url_for('login')) 


@app.route('/')
def index():
    if 'user_email' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('inicio')) 

@app.route('/inicio')
def inicio():
    info = f"¡Hola {session.get('user_nombre', 'invitado')}! Aquí encontrarás información fascinante... (Sesión iniciada como: {session.get('user_email', 'N/A')})"
    return render_template('inicio.html', title='Inicio', info=info)


@app.route('/animales_exoticos')
def animales_exoticos():
    contenido = "Bienvenido a la pestaña dedicada a los animales exóticos. Aquí descubrirás especies únicas de todo el planeta."
    return render_template('animales_exoticos.html', title='Animales Exóticos', content=contenido)

@app.route('/vehiculos_antiguos')
def vehiculos_antiguos():
    contenido = "Explora la historia de los automóviles clásicos, desde los modelos T hasta los muscle cars de la época dorada. Una ventana al pasado del transporte."
    return render_template('vehiculos_antiguos.html', title='Vehículos Antiguos', content=contenido)

@app.route('/maravillas_del_mundo')
def maravillas_del_mundo():
    contenido = "Viaja a través de la historia y admira las siete grandes maravillas del mundo, tanto antiguas (como la Gran Pirámide de Guiza) como modernas (como la Gran Muralla China)."
    return render_template('maravillas_del_mundo.html', title='Maravillas del Mundo', content=contenido)

@app.route('/acerca_de')
def acerca_de():
    contenido = "Este sitio web fue desarrollado como ejemplo de una aplicación de autenticación y enrutamiento básica utilizando el framework Flask de Python. Su propósito es ser una herramienta educativa y de demostración."
    return render_template('acerca_de.html', title='Acerca de...', content=contenido)


@app.route('/registrame', methods=['GET', 'POST'])
def registrame():
    if 'user_email' in session:
        return redirect(url_for('inicio'))

    if request.method == 'POST':
        nombre = request.form.get('nombre') 
        apellido = request.form.get('apellido')
        email = request.form.get('contacto') 
        password = request.form.get('contrasena') 
        confirmPassword = request.form.get('confirmaContraseña') 
        
        if not all([nombre, apellido, email, password, confirmPassword]):
            flash('Todos los campos son obligatorios.', 'danger')
            return redirect(url_for('registrame'))
        
        for user in USERS:
            if user['email'] == email:
                flash(f'El correo electrónico "{email}" ya está registrado.', 'danger')
                return redirect(url_for('registrame'))

        if password != confirmPassword:
            flash("La contraseña no coincide", 'danger')
            return redirect(url_for('registrame'))
        
        new_user = {
            'nombre': nombre,
            'apellido': apellido,
            'email': email,
            'password': password 
        }
        USERS.append(new_user) 
        
        flash('¡Registro exitoso! Ahora puedes iniciar sesión con tu email y contraseña.', 'success')
        return redirect(url_for('login'))

    return render_template('registro.html', title='Registro', no_menu=True)

@app.route('/registro')
def registro():
    return redirect(url_for('registrame'))

if __name__ == '__main__':
    app.run(debug=True)
