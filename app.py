
# app.py

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__,template_folder='template')
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        return render_template('confirmacion.html', nombre=nombre, email=email)
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True , port=5017)
