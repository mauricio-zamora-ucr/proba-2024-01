from flask import Flask, redirect, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def inicio():
    x1 = float(request.form.get('valor1',0))
    x2 = float(request.form.get('valor1',0))
    y = float(request.form.get('valor1',0))

    if request.method == 'POST':
        y = x1 + x2

    return render_template('index.html', valor1=x1, valor2=x2, resultado=y)

if __name__ == '__main__':
    app.run(debug=True)