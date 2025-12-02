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
                estoque INTEGER NOT NULL,
                frete TEXT)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS carrinho (
                cod_carrinho INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL, 
                cod TEXT NOT NULL, 
                preco REAL NOT NULL, 
                quantidade INTEGER NOT NULL,
                frete TEXT)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedido (
                num_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
                data DATETIME NOT NULL,
                cliente_cpf TEXT NOT NULL,
                total REAL NOT NULL,
                status TEXT NOT NULL,
                cod_carrinho INTEGER NOT NULL,
                produtos TEXT NOT NULL)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pagamento (
                id_pagamento INTEGER PRIMARY KEY AUTOINCREMENT,
                id_pedido TEXT FOREIGNH KEY NOT NULL,
                forma_pagamento TEXT NOT NULL, 
                valor_pago REAL NOT NULL,
                data_pagamento DATE NOT NULL)
        
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS relatorio_faturamento (
                id_relatorio_faturamento INTEGER PRIMARY KEY AUTOINCREMENT,
                data_relatorio DATE NOT NULL,
                mes_referencia DATE NOT NULL,
                quantidade_vendas INTEGER NOT NULL, 
                valor_arrecadado TEXT NOT NULL)
""")


conexao.commit()
conexao.close()
