import sqlite3

conexao = sqlite3.connect("loja virtual.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS cliente (
                nome TEXT,
                email TEXT, 
                cpf INTEGER PRIMARY KEY,
                rua TEXT, 
                cep TEXT)
""")
conexao.commit()
conexao.close()

conexao = sqlite3.connect("loja virtual.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS produto (
                nome TEXT,
                cod TEXT PRIMARY KEY, 
                categoria TEXT,
                preco REAL, 
                estoque INTEGER)
""")
conexao.commit()
conexao.close()

conexao = sqlite3.connect("loja virtual.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS carrinho (
                id_carrinho INTEGER PRIMARY KEY,
                id_item_carrinho TEXT,
                quantidade_itens TEXT, 
                subtotal REAL)
""")
conexao.commit()
conexao.close()

conexao = sqlite3.connect("loja virtual.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedido (
                num_pedido INTEGER PRIMARY KEY,
                id_carrinho INTEGER,
                valor_pedido REAL,
                cpf INTEGER, 
                forma_pagamento TEXT,
                frete TEXT, 
                desconto TEXT)
""")
conexao.commit()
conexao.close()

conexao = sqlite3.connect("loja virtual.db")
cursor = conexao.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS pagamento (
                id_pagamento INTEGER PRIMARY KEY,
                id_pedido TEXT,
                forma_pagamento TEXT, 
                status TEXT,
                data_pagamento DATE)
""")
conexao.commit()
conexao.close()
