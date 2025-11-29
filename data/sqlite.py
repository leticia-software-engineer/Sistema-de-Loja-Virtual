import sqlite3

conexao = sqlite3.connect("loja virtual.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS cliente (
                nome TEXT NOT NULL,
                email TEXT NOT NULL, 
                cpf TEXT PRIMARY KEY NOT NULL,
                rua TEXT NOT NULL, 
                cep TEXT NOT NULL)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS produto (
                nome TEXT NOT NULL,
                cod TEXT PRIMARY KEY NOT NULL, 
                categoria TEXT NOT NULL,
                preco REAL NOT NULL, 
                estoque INTEGER NOT NULL)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS carrinho (
                cod_carrinho INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL, 
                cod TEXT NOT NULL, 
                preco REAL NOT NULL, 
                quantidade INTEGER NOT NULL)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedido (
                num_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
                cod_carrinho INTEGER FOREIGNH KEY NOT NULL,
                valor_pedido REAL NOT NULL,
                cpf INTEGER FOREIGNH KEY NOT NULL, 
                forma_pagamento TEXT FOREIGNH KEY NOT NULL,
                frete TEXT NOT NULL, 
                desconto TEXT)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pagamento (
                id_pagamento INTEGER PRIMARY KEY AUTOINCREMENT,
                id_pedido TEXT FOREIGNH KEY NOT NULL,
                forma_pagamento TEXT NOT NULL, 
                status TEXT NOT NULL,
                data_pagamento DATE NOT NULL)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS relatorio (
                id_relatorio INTEGER PRIMARY KEY AUTOINCREMENT,
                data DATE NOT NULL,
                quantidade_vendas INTEGER NOT NULL, 
                status TEXT NOT NULL,
                id_frete TEXT FOREIGNH KEY NOT NULL)
""")


conexao.commit()
conexao.close()
