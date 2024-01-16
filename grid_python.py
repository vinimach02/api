from flask import Flask, render_template
import pymssql

app = Flask(__name__)

# Configuração do banco de dados SQL Server (substitua pelos seus dados)
db_config = {
    'server': 'seu_servidor',
    'database': 'sua_base_de_dados',
    'user': 'seu_usuario',
    'password': 'sua_senha',
    'port': 1433,  # Porta padrão do SQL Server
}

def obter_dados_sql():
    conn = pymssql.connect(**db_config)
    cursor = conn.cursor()

    # Substitua 'sua_tabela' pelo nome da sua tabela
    cursor.execute('SELECT * FROM sua_tabela')
    dados = cursor.fetchall()

    conn.close()

    return dados

@app.route('/')
def exibir_dados():
    dados = obter_dados_sql()
    return render_template('grid.html', dados=dados)

if __name__ == '__main__':
    app.run(debug=True)
