from flask import Flask, redirect, render_template, request
import base64
from io import BytesIO
from matplotlib.figure import Figure
from statistics import NormalDist


app = Flask(__name__)

@app.route('/dnpm', methods=['GET', 'POST'])
def calcular_probabilidad_menor():
    x = float(request.form.get('x',0))
    media = float(request.form.get('media',0))
    ds = float(request.form.get('desviacion',0))
    resultado = 0
    if request.method == 'POST':
        distribucion_normal = NormalDist()
        if ds != 0:
            z = (x-media)/ds
            resultado = '{:.2f}%'.format(distribucion_normal.cdf(z)*100) 
        else:
            resultado = 'N/A'
 
    return render_template('dnprobmenor.html',x=0,media=media, desviacion=ds, resultado=resultado)


@app.route('/', methods=['GET', 'POST'])
def inicio():
    x1 = float(request.form.get('valor1',0))
    x2 = float(request.form.get('valor1',0))
    y = float(request.form.get('valor1',0))

    if request.method == 'POST':
        y = x1 + x2

    return render_template('index.html', valor1=x1, valor2=x2, resultado=y)


@app.route("/chart")
def hello():
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"

if __name__ == '__main__':
    app.run(debug=True)