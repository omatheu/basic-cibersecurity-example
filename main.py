from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Conexão global com o banco (má prática!)
conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()

# Cria a tabela sem validação (má prática!)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
''')
conn.commit()

@app.route('/greet')
def greet():
    name = request.args.get('name', '')
    return f"<h1>Hello, {name}!</h1>"

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    # EXECUTA VÁRIAS INSTRUÇÕES (ALTAMENTE PERIGOSO)
    query = f"""
    INSERT INTO users (username, password) VALUES ('{username}', '{password}');
    """
    cursor.executescript(query)
    conn.commit()
    
    return jsonify({"message": "User registered!"})

@app.route('/login', methods=['POST'])
def login():
    # NÃO há hashing de senha ou validação
    data = request.get_json()
    username = data['username']
    password = data['password']

    # SQL Injection aqui também
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()

    if user:
        # Expondo dados sensíveis
        return jsonify({"message": "Login successful", "user": user})
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route('/debug')
def debug():
    # Endpoint expõe informações sensíveis (debug)
    return jsonify({
        "headers": dict(request.headers),
        "args": request.args,
        "env": dict(request.environ)
    })

if __name__ == '__main__':
    # Executando com debug ativado (má prática)
    app.run(debug=True)

