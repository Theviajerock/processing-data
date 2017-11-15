from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
@app.route('/index', methods=["POST","GET"])
def index():
    if request.method == "POST":
        cedula= request.form['cedula']
        usuario = request.form['usuario']
        return render_template('result.html', cedula=cedula, usuario=usuario)
    else:
        return render_template('index.html')

app.run(debug=True, host="0.0.0.0", port=8080)

