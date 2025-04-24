from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_imc', methods=['POST'])
def calcular_imc():
    altura = float(request.form['altura'])
    peso = float(request.form['peso'])

    imc = round(peso /(altura **2),2)

    if imc < 18.5:
        diagnostico = 'Abaixo do peso'
    elif imc < 24.9:
        diagnostico = 'Peso normal'
    elif imc < 29.9:
        diagnostico = 'Acima do peso'
    else:
        diagnostico = 'Obeso'

    # Renderiza o templates HTML com o resultado do IMC e diagnóstico
    return render_template('index.html', imc=imc, diagnostico=diagnostico)

if __name__ == '__main__':
    app.run(debug=True)