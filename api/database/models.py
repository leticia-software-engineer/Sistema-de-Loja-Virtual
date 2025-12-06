from sqlalchemy import create_engine, MetaData, Table

meu_banco_de_dados = "sqlite:///loja virtual.db"
engine = create_engine(meu_banco_de_dados, echo=True)

metadata = MetaData()

produto = Table('produto', metadata, autoload_with=engine)
pedido = Table('pedido', metadata, autoload_with=engine)
cliente = Table('cliente', metadata, autoload_with=engine)
pagamento = Table('pagamento', metadata, autoload_with=engine)
carrinho = Table('carrinho', metadata, autoload_with=engine)

