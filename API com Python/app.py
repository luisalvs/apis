from flask import Flask, jsonify, request # importando lib flask e modulo json para retornar no formato json

# Criando API com Python - Lugar para disponibilizar recursos e/ou funcionalidades

# 1 - Objetivo --> Criar uma api que disponibiliza a consulta, criação, edição e exclusão de livros
# 2 - URL Base --> localhost
# 3 - Endpoints:
    # localhost/livros (GET)
    # localhost/livros/id (GET)
    # localhost/livros/id (PUT)
    # localhost/livros/id (DELETE)
# 4 - Recursos - Livros


app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O Senhor dos Anéis - A Sociedade do Anel ',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'título': 'James Clear',
        'autor': 'Hábitos Atômicos'

    }
]

# Consultar (todos)
@app.route('/livros', methods=['GET']) # acrescenta o paremetro/rota ao final da url, methods permite somente o metodo escolhido ser utilizado

def obter_livros():
    return jsonify(livros) # retorna o arquivo no formato json

# Consultar (id)
@app.route('/livros/<int:id>', methods=['GET']) # no campo <> passa o parametro do item no caso interger
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id: # pega o campo id na lista de livros
            return jsonify(livro)
        
# Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# Criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livro[indice]
    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True) # Inicializar a api