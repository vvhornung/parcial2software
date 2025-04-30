from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route('/factorial/<int:val>')
def factorial(val):
    if val < 0:
        return "<h2>No existe el factorial de un numero negativo.</h2>"
    else:
        resultado = 1
        for i in range(1, val + 1):
            resultado *= i
        return f"<h2>El factorial de {val} es: {resultado}</h2>"

if __name__ == '__main__':
    aplicacion.run(debug=True)
