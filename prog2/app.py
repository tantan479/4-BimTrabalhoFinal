from flask import Flask, request, render_template
from config.Config import Config
from config.Database import Database
from dao.UsuarioDao import UsuarioDao
config = Config()
database = Database(config.config)
dao = UsuarioDao(database.conn)
lista = dao.selecionarUsuarios()
# tela = Table(lista) fazer tela 


# Raphael e Renato

app = Flask(__name__)

@app.route('/', methods=['POST'])
def form():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    return f"Seu nome é {nome} {email} {senha}"
    


@app.route('/', methods=['GET'])
def get():
    return render_template("form.html")



if __name__ == '__main__':
    app.run()
    


