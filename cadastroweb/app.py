from flask import Flask, render_template, request, redirect, url_for, flash, g
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import os

DATABASE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance', 'users.db')

app = Flask(__name__)
app.secret_key = 'troque_para_algo_secreto_em_producao'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with open('schema.sql', 'r') as f:
            db.executescript(f.read())
        db.commit()

@app.route('/')
def index():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        cpf = request.form.get('cpf')
        senha = request.form['senha']
        senha_hash = generate_password_hash(senha)
        db = get_db()
        try:
            db.execute("INSERT INTO usuario (nome,email,senha_hash,cpf) VALUES (?,?,?,?)",
                       (nome,email,senha_hash,cpf))
            db.commit()
            flash('Usuário cadastrado com sucesso!', 'success')
            return redirect(url_for('register'))
        except sqlite3.IntegrityError as e:
            flash('Erro: email ou CPF já cadastrado.', 'error')
    return render_template('register.html')

if __name__ == '__main__':
    os.makedirs(os.path.join(os.path.dirname(__file__), 'instance'), exist_ok=True)
    if not os.path.exists(DATABASE):
        init_db()
    app.run(debug=True)
