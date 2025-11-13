import sqlite3

banco_de_dados = sqlite3.connect("AbraCaxi.db")

cursor = banco_de_dados.cursor()

cursor.execute("CREATE TABLE produto (nome text, cod integer, categoria text, preco_unitario real, estoque integer)")

cursor.execute("CREATE TABLE cliente (nome text, email text, cpf integer, cidade text, cep integer, uf text)")
cursor.execute("CREATE TABLE pedidos (total real, status text, )")
cursor.execute("CREATE TABLE pagamentos (nome text, cod integer, categoria text, preco_unitario real, estoque integer)")
cursor.execute("CREATE TABLE fretes (nome text, cod integer, categoria text, preco_unitario real, estoque integer)")
cursor.execute("CREATE TABLE relatorios (nome text, cod integer, categoria text, preco_unitario real, estoque integer)")
