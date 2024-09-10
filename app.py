#API
# objetivo - Criar uma api que disponibiliza a consulta, criacao, edicao e exclusao de livros

# url base - localhost

# endpoints - 
    # - localhost/livros (GET)
    # - localhost/livros (POST)
    # - localhost/livros/id (GET)
    # - localhost/livros/id (PUT)
    # - localhost/livros/id (DELETE)
    
# quais recursos - Livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'o senhor dos aneis',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e a pedra filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'titulo': 'James Clear',
        'autor': 'Habitos Atomicos'
    },
]

#Consultar(todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

#Consultar(ID)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

#Editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livros_por_id(id):
   livro_alterado = request.get_json()
   for indice,livro, in enumerate(livros):
       if livro.get('id') == id:
           livros[indice].update(livro_alterado)
           return jsonify(livros[indice])
       
#Criar
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify (livros)
    
    
#excuir
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)
    

app.run(port=5000,host='localhost',debug=True)