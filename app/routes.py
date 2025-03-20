from flask import Blueprint, render_template, request, jsonify
from .extract_b import extrair_valores_e_contexto

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/extract', methods=['POST'])
def extract():
    data = request.get_json()
    print("JSON Recebido:", data)  # 👈 Para debug

    if not data or 'texto' not in data:
        return jsonify({'error': 'Texto vazio'}), 400
    
    resultados = extrair_valores_e_contexto(data['texto'])
    print("Resultados:", resultados)  # 👈 Para debug

    return jsonify(resultados)

# Rota para Favicon
@main.route('/favicon.ico')
def favicon():
    from flask import send_from_directory
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')
