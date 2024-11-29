from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


@app.route('/api/dados', methods=['POST'])
def receber_dados():
    try:
        # Recebe o payload em JSON
        data = request.get_json()
        
        # Extrai os dados
        ph = data.get('ph')
        turbidez = data.get('turbidez')
        condutividade = data.get('condutividade')
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        
        # Verifica se todos os campos obrigatórios foram fornecidos
        if ph is None or turbidez is None or condutividade is None:
            return jsonify({'message': 'Dados incompletos, por favor envie ph, turbidez e condutividade.'}), 400
        
        # Cria uma nova entrada no banco de dados
        nova_entrada = SensorData(
            ph=ph,
            turbidez=turbidez,
            condutividade=condutividade,
            latitude=latitude,
            longitude=longitude
        )
        db.session.add(nova_entrada)
        db.session.commit()
        
        return jsonify({'message': 'Dados recebidos com sucesso!'}), 201
    except Exception as e:
        return jsonify({'message': f'Erro ao processar os dados: {str(e)}'}), 500