# app.py
from flask import Flask, render_template, request, jsonify
from operacoes import Calculadora

app = Flask(__name__)
calculadora = Calculadora() # Cria uma instância da sua calculadora Python

@app.route('/')
def index():
    """
    Rota principal que renderiza a página HTML da calculadora.
    """
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Rota que recebe os dados da operação do front-end via POST,
    executa o cálculo no backend Python e retorna o resultado.
    """
    data = request.get_json() # Pega os dados JSON enviados pelo front-end

    num1 = float(data['num1'])
    num2 = float(data['num2'])
    operation = data['operation']

    result = None
    error = None

    if operation == 'soma':
        result = calculadora.somar(num1, num2)
    elif operation == 'subtracao':
        result = calculadora.subtrair(num1, num2)
    elif operation == 'multiplicar':
        result = calculadora.multiplicar(num1, num2)
    elif operation == 'dividir':
        # A função dividir já trata o erro de divisão por zero
        temp_result = calculadora.dividir(num1, num2)
        if isinstance(temp_result, str) and "Erro" in temp_result:
            error = temp_result
        else:
            result = temp_result
    elif operation == 'potenciacao':
        result = calculadora.potenciacao(num1, num2)
    else:
        error = "Operação inválida."

    # Retorna o resultado ou erro como JSON para o front-end
    if error:
        return jsonify({'error': error}), 400 # Retorna 400 Bad Request em caso de erro
    else:
        return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True) # debug=True permite recarregamento automático e depuração