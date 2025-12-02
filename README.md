# Sistema-de-Loja-Virtual - AbraCaxi

O AbraCaxi é um projeto de POO que simula um e-commerce no qual é possível realizar compras de produtos diversos. No sistema é possível, escolher os produtos a comprar, adicionar ao carrinho, realizar a compra, confirmar o pagamento, visualizar os cupons disponíveis, os produtos mais vendidos e a tabela de valores de frete conforme o cep. O objetivo do projeto é aplicar de forma prática conceitos importantes da programação orientada a objetos utilizando a linguagem python para elaboração do back end, empregando conceitos importantes da programação orientada a objetos, tais como: herança, encapsulamento, validações e composição.

# Estrutura 

loja virtual/
├── data/<br>
│   ├── loja virtual.db<br>
│   └── sqlite.py<br>
|<br>
├── Fonte/<br>
│   ├── _pycache_/<br>
│   ├── abracaxi.py<br>
│   ├── carrinho.py<br>
│   ├── cliente.py<br>
│   ├── configuracoes.py<br>
│   ├── cupom.py<br>
│   ├── expedicao.py<br>
│   ├── frete.py<br>
│   ├── pagamento.py<br>
│   ├── pedido.py<br>
│   ├── produto.py<br>
│   └── relatorio.py<br>
|<br>
├── Requisitos/<br>
|<br>
├── Rotas/<br>
│   ├── rotas_aut.py<br>
│   └── rotas.py<br>
|
├── Utilitarios/<br>
│   ├── testes/<br>
│   │   ├── pytest.ini<br>
│   │   └── testes.py<br>
│   ├── calculos.py<br>
│   └── requirements.txt<br>
|<br>
├── LICENSE<br>
├── main.py<br>
└── README.md<br>

# UML Textual

| Classe        | Métodos                                                   | Atributos                                                    | Relacionamentos               |
|---------------|-----------------------------------------------------------|--------------------------------------------------------------|-------------------------------|
| **Produto**       | ajustar_estoque, CRUD                                  | nome, categoria, preco_unitario, estoque, cod                | Pedido, Carrinho, ItemCarrinho, Configuracoes.                       |
| **Cliente**       | valida_email, valida_cpf, valida_cep, CRUD             | nome, email, cpf, cidade, cep, uf                             | Pedido, Frete.                          |
| **Carrinho**      | adicionar, remover, alterar_quant                      | produto, quantidade                                           | Produto, ItemCarrinho                      |
| **Pedido**        | cancelar, gerar_nota                                   | cliente, itens, frete, desconto, total, status                | Carrinho, Cliente, CupomDesconto, Frete, Expedição, Relatorio. |
| **Pagamento**     | validar, registrar                                     | forma_pagamento, data, status                                 | Pedido.                       |
| **Frete**         | calcular_por_cep                                       | prazo, cep, valor                                             | Cliente, Pedido               |
| **Expedição**     | gerar_cod, marcar_entregue                             | cod_entrega, data_entrega, status_entrega                     | Pedido            |
| **Relatório**     | faturamento_periodo, ranking, vendas_por_estado, vendas_por_categoria, pedidos_status | dia, mes, ano                                                 | Pedido, Frete, Pagamento.                        |
| **CupomDesconto** | aplicar_desconto                                       | cod_cupom, valor, validade, caso_uso, categoria               | Pedido                             |
| **Configuracoes** | politica_cancelamento, perfil, tabela_frete, top_produtos, validade_cupons, limite_parcelas | —                                                            | Frete, Produto, CupomDesconto |
|