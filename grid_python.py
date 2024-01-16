from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados SQLite (substitua pela sua configuração)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exemplo.db'
db = SQLAlchemy(app)

# Modelo para a tabela de dados
class Dado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(50))

# Rota para a página HTML com o grid
@app.route('/')
def exibir_grid():
    dados = Dado.query.all()
    return render_template('grid.html', dados=dados)

if __name__ == '__main__':
    # Criação do banco de dados e execução do servidor
    db.create_all()
    app.run(debug=True)
