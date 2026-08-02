import os
import sqlite3
from functools import wraps

import requests
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, g
from werkzeug.security import generate_password_hash, check_password_hash

# ---------------------------------------------------------------------------
# Configuração da aplicação
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "database.db")

app = Flask(__name__)

# A SECRET_KEY é lida do ambiente. Em produção, defina a variável de
# ambiente SECRET_KEY. Caso não exista, usamos um valor padrão apenas
# para facilitar a execução local/dos exercícios.
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "chave-secreta-para-desenvolvimento")

# DEBUG=False no ambiente de produção (conforme solicitado no exercício).
# Controlado pela variável de ambiente FLASK_DEBUG (padrão: desligado).
app.config["DEBUG"] = os.environ.get("FLASK_DEBUG", "0") == "1"

STATUS_OPCOES = ["Pendente", "Em andamento", "Concluída"]
STATUS_CORES = {
    "Pendente": "warning",       # amarelo
    "Em andamento": "primary",   # azul
    "Concluída": "success",      # verde
}


# ---------------------------------------------------------------------------
# Banco de dados (SQLite)
# ---------------------------------------------------------------------------
def get_db():
    """Abre (ou reaproveita) a conexão SQLite da requisição atual."""
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    """Cria as tabelas usuarios e tarefas caso não existam."""
    db = sqlite3.connect(DATABASE)
    db.executescript(
        """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            status TEXT NOT NULL DEFAULT 'Pendente',
            usuario_id INTEGER NOT NULL,
            FOREIGN KEY (usuario_id) REFERENCES usuarios (id) ON DELETE CASCADE
        );
        """
    )
    db.commit()
    db.close()


# ---------------------------------------------------------------------------
# Autenticação / proteção de rotas
# ---------------------------------------------------------------------------
def login_requerido(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "usuario_id" not in session:
            flash("Você precisa estar logado para acessar essa página.", "warning")
            return redirect(url_for("login"))
        return func(*args, **kwargs)

    return wrapper


@app.context_processor
def injetar_contexto():
    return {
        "usuario_logado": session.get("usuario_nome"),
        "status_opcoes": STATUS_OPCOES,
        "status_cores": STATUS_CORES,
    }


# ---------------------------------------------------------------------------
# Rotas de autenticação
# ---------------------------------------------------------------------------
@app.route("/")
def index():
    if "usuario_id" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")

        if not nome or not email or not senha:
            flash("Preencha todos os campos.", "danger")
            return render_template("registro.html")

        db = get_db()
        existente = db.execute("SELECT id FROM usuarios WHERE email = ?", (email,)).fetchone()
        if existente:
            flash("Já existe uma conta com esse e-mail.", "danger")
            return render_template("registro.html")

        senha_hash = generate_password_hash(senha)
        db.execute(
            "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
            (nome, email, senha_hash),
        )
        db.commit()
        flash("Conta criada com sucesso! Faça login.", "success")
        return redirect(url_for("login"))

    return render_template("registro.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")

        db = get_db()
        usuario = db.execute("SELECT * FROM usuarios WHERE email = ?", (email,)).fetchone()

        if usuario is None or not check_password_hash(usuario["senha"], senha):
            flash("E-mail ou senha inválidos.", "danger")
            return render_template("login.html")

        session.clear()
        session["usuario_id"] = usuario["id"]
        session["usuario_nome"] = usuario["nome"]
        flash(f"Bem-vindo(a), {usuario['nome']}!", "success")
        return redirect(url_for("dashboard"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("Você saiu da sua conta.", "info")
    return redirect(url_for("login"))


# ---------------------------------------------------------------------------
# Frase motivacional (API externa)
# ---------------------------------------------------------------------------
def buscar_frase_motivacional():
    try:
        resposta = requests.get("https://api.adviceslip.com/advice", timeout=4)
        resposta.raise_for_status()
        dados = resposta.json()
        return dados.get("slip", {}).get("advice")
    except (requests.RequestException, ValueError):
        return "Não foi possível carregar a frase do dia. Tente novamente mais tarde."


# ---------------------------------------------------------------------------
# Dashboard / CRUD de tarefas
# ---------------------------------------------------------------------------
@app.route("/dashboard")
@login_requerido
def dashboard():
    db = get_db()
    filtro_status = request.args.get("status")

    query = "SELECT * FROM tarefas WHERE usuario_id = ?"
    params = [session["usuario_id"]]

    if filtro_status in STATUS_OPCOES:
        query += " AND status = ?"
        params.append(filtro_status)

    query += " ORDER BY id DESC"
    tarefas = db.execute(query, params).fetchall()

    frase = buscar_frase_motivacional()

    return render_template(
        "dashboard.html",
        tarefas=tarefas,
        frase=frase,
        filtro_status=filtro_status,
    )


@app.route("/api/tarefas")
@login_requerido
def api_tarefas():
    """Retorna as tarefas do usuário em JSON, com filtro opcional por status."""
    db = get_db()
    filtro_status = request.args.get("status")

    query = "SELECT * FROM tarefas WHERE usuario_id = ?"
    params = [session["usuario_id"]]

    if filtro_status in STATUS_OPCOES:
        query += " AND status = ?"
        params.append(filtro_status)

    query += " ORDER BY id DESC"
    tarefas = db.execute(query, params).fetchall()

    return jsonify([dict(t) for t in tarefas])


@app.route("/api/progresso")
@login_requerido
def api_progresso():
    """Retorna a contagem de tarefas por status, para os gráficos do dashboard de progresso."""
    db = get_db()
    linhas = db.execute(
        "SELECT status, COUNT(*) as total FROM tarefas WHERE usuario_id = ? GROUP BY status",
        (session["usuario_id"],),
    ).fetchall()

    contagem = {status: 0 for status in STATUS_OPCOES}
    for linha in linhas:
        contagem[linha["status"]] = linha["total"]

    return jsonify(contagem)


@app.route("/dashboard/progresso")
@login_requerido
def dashboard_progresso():
    return render_template("progresso.html")


@app.route("/nova_tarefa", methods=["GET", "POST"])
@login_requerido
def nova_tarefa():
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        descricao = request.form.get("descricao", "").strip()
        status = request.form.get("status", "Pendente")

        if not titulo:
            flash("O título da tarefa é obrigatório.", "danger")
            return render_template("form_tarefa.html", modo="nova", tarefa=None)

        if status not in STATUS_OPCOES:
            status = "Pendente"

        db = get_db()
        db.execute(
            "INSERT INTO tarefas (titulo, descricao, status, usuario_id) VALUES (?, ?, ?, ?)",
            (titulo, descricao, status, session["usuario_id"]),
        )
        db.commit()
        flash("Tarefa criada com sucesso!", "success")
        return redirect(url_for("dashboard"))

    return render_template("form_tarefa.html", modo="nova", tarefa=None)


@app.route("/editar/<int:id>", methods=["GET", "POST"])
@login_requerido
def editar_tarefa(id):
    db = get_db()
    tarefa = db.execute(
        "SELECT * FROM tarefas WHERE id = ? AND usuario_id = ?",
        (id, session["usuario_id"]),
    ).fetchone()

    if tarefa is None:
        flash("Tarefa não encontrada.", "danger")
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        descricao = request.form.get("descricao", "").strip()
        status = request.form.get("status", tarefa["status"])

        if not titulo:
            flash("O título da tarefa é obrigatório.", "danger")
            return render_template("form_tarefa.html", modo="editar", tarefa=tarefa)

        if status not in STATUS_OPCOES:
            status = tarefa["status"]

        db.execute(
            "UPDATE tarefas SET titulo = ?, descricao = ?, status = ? WHERE id = ? AND usuario_id = ?",
            (titulo, descricao, status, id, session["usuario_id"]),
        )
        db.commit()
        flash("Tarefa atualizada com sucesso!", "success")
        return redirect(url_for("dashboard"))

    return render_template("form_tarefa.html", modo="editar", tarefa=tarefa)


@app.route("/excluir/<int:id>", methods=["POST"])
@login_requerido
def excluir_tarefa(id):
    db = get_db()
    db.execute(
        "DELETE FROM tarefas WHERE id = ? AND usuario_id = ?",
        (id, session["usuario_id"]),
    )
    db.commit()
    flash("Tarefa excluída.", "info")
    return redirect(url_for("dashboard"))


@app.route("/concluir/<int:id>", methods=["POST"])
@login_requerido
def concluir_tarefa(id):
    db = get_db()
    db.execute(
        "UPDATE tarefas SET status = 'Concluída' WHERE id = ? AND usuario_id = ?",
        (id, session["usuario_id"]),
    )
    db.commit()
    flash("Tarefa marcada como concluída!", "success")
    return redirect(url_for("dashboard"))


# ---------------------------------------------------------------------------
# Ponto de entrada
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    init_db()
    app.run(debug=app.config["DEBUG"])
else:
    # Garante que o banco exista também quando importado (ex.: gunicorn, testes)
    init_db()
