CREATE TABLE IF NOT EXISTS usuario (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  senha_hash TEXT NOT NULL,
  cpf TEXT UNIQUE,
  telefone TEXT,
  perfil TEXT DEFAULT 'usuario',
  criado_em DATETIME DEFAULT (datetime('now'))
);
