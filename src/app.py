from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/blog', methods=['GET'])
def blog():
    return render_template('blog.html')

@app.route('/projetista', methods=['GET'])
def proj():
    return render_template('projetista.html')

@app.route('/calculadora', methods=['GET'])
def cal():
    return render_template('calculadora.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        expression = request.json.get('expression')
        result = eval(expression.replace(',', '.'))
        return jsonify(result=result)
    except:
        return jsonify(result="Erro")