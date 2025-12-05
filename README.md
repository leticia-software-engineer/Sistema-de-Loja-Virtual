# Sistema-de-Loja-Virtual - AbraCaxi

O AbraCaxi é um projeto de POO que simula um e-commerce no qual é possível realizar compras de produtos físicos e digitais. No sistema é possível escolher os produtos, adicionar ao carrinho, realizar a compra, confirmar o pagamento, acompanhar a entrega, conferir os produtos mais vendidos e a tabela de valores de frete conforme o cep, gerar relatórios de faturamento diário e mensal, status de pedidos, vendas e outros. O objetivo do projeto é aplicar de forma prática conceitos importantes da programação orientada a objetos empregando conceitos importantes tais como: herança, encapsulamento, validações e composição. As principais tecnologias utilizadas no desenvolvimento do projeto foram: python, como linguagem de programação, sqlite, para a persistência dos dados e FastApi com framework para a criação da API.

# Estrutura 

loja virtual/
├── data/<br>
│   ├──ceps_cotacoes_ceara.json<br>
│   └── sqlite.py<br>
|<br>
├── Fonte/<br>
│   ├── _pycache_/<br>
│   ├── abracaxi.py<br>
│   ├── carrinho.py<br>
│   ├── cliente.py<br>
│   ├── configuracoes.py<br>
│   ├── expedicao.py<br>
│   ├── frete.py<br>
│   ├── pagamentos.py<br>
│   ├── pedido.py<br>
│   ├── produto_digital.py<br>
│   ├── produto_fisico.py<br>
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
│   ├── LICENSE <br>
│   └── requirements.txt<br>
|<br>
├── loja virtual.db<br>
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

Ceps disponíveis para teste 
63210000     32.0             18
63260000     30.0              7
63240000     37.0             12
63136000     30.0             25
63137000     32.0              5
63180000     10.0             29
63138000     30.0             14
63139000     30.0             22
63510000     20.0              9
63511000     40.0              3
63512000     20.0             30
63010900     10.0             13
63010905     20.0              8
63250000     40.0             19
63255000     20.0              4
63165000     10.0             27