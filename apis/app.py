from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import urllib.parse

app = Flask(__name__)

usuario = 'root'
senha = 'Max@Gustavo2025'
servidor = '95.111.231.72'
database = 'SISTEMA'

senha_codificada = urllib.parse.quote_plus(senha)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mariadb+mysqlconnector://{usuario}:{senha_codificada}@{servidor}/{database}'

db = SQLAlchemy(app)

class Tokens(db.Model):
    __tablename__= 'RECAPTCHA'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, default=datetime)
    usado = db.Column(db.String(1))
    
@app.route('/count', methods=['GET'])
def get_token():
    tempo = datetime.now() - timedelta(seconds=90)
    total = Tokens.query.filter(
        Tokens.data >= tempo,
        Tokens.usado == 'N'
    ).count()
    
    return jsonify({
        'qtde': total
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)