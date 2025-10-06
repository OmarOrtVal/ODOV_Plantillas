from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    arr = ["Padilla","Renteria","Soto"]
    autor = "Omar Daniel Ortega Valtierra"
    return render_template("plantilla.html", nombre = autor, amigos = arr)

@app.route("/ciudades")
def ciudades():
    arr = ["Italia","Bangkok","New York"]
    autor = "Omar Daniel Ortega Valtierra"
    return render_template("plantilla1.html", nombre = autor, ciudades = arr)

@app.route("/colores")
def colores():
    arr = ["Azul","Rosa","Rojo"]
    autor = "Omar Daniel Ortega Valtierra"
    return render_template("plantilla2.html", nombre = autor, colores = arr)

if __name__ == "__main__":
    app.run(debug=True)