# Sistema-de-Loja-Virtual - AbraCaxi

O AbraCaxi é um projeto de POO que simula um e-commerce no qual é possível realizar compras de produtos diversos. No sistema é possível, escolher os produtos a comprar, adicionar ao carrinho, realizar a compra, confirmar o pagamento, visualizar os cupons disponíveis, os produtos mais vendidos e a tabela de valores de frete conforme o cep.
As tecnologias utilizadas no desenvolvimento do AbraCaxi são: a linguagem python para elaboração do back end, empregando conceitos importantes da programação orientada a objetos, tais como: herança, encapsulamento, validações e composição.

# UML Textual

| Classe        | Métodos                                                   | Atributos                                                    | Relacionamentos               |
|---------------|-----------------------------------------------------------|--------------------------------------------------------------|-------------------------------|
| **Produto**       | ajustar_estoque, CRUD                                  | nome, categoria, preco_unitario, estoque, cod                | —                             |
| **Cliente**       | valida_email, valida_cpf, valida_cep, CRUD             | nome, email, cpf, cidade, cep, uf                             | —                             |
| **Carrinho**      | adicionar, remover, alterar_quant                      | produto, quantidade                                           | Produto                       |
| **Pedido**        | cancelar, gerar_nota                                   | cliente, itens, frete, desconto, total, status                | Carrinho, Cliente, CupomDesconto, Frete, Expedição |
| **Pagamento**     | validar, registrar                                     | forma_pagamento, data, status                                 | Pedido                        |
| **Frete**         | calcular_por_cep                                       | prazo, cep, valor                                             | Cliente, Pedido               |
| **Expedição**     | gerar_cod, marcar_entregue                             | cod_entrega, data_entrega, status_entrega                     | Pedido, Entregador            |
| **Relatório**     | faturamento_periodo, ranking, vendas_por_estado, ticket_medio, vendas_por_categoria, pedidos_status | dia, mes, ano                                                 | Pedido                        |
| **CupomDesconto** | aplicar_desconto                                       | cod_cupom, valor, validade, caso_uso, categoria               | —                             |
| **Configurações** | politica_cancelamento, perfil, tabela_frete, top_produtos, validade_cupons, limite_parcelas | —                                                            | Frete, Produto, CupomDesconto |
| **Vendedor**      | valida_email, valida_cnpj, CRUD                        | nome, email, cnpj, loja                                       | Produto                       |
| **Entregador**    | valida_email, valida_cpf, CRUD                         | nome, email, cpf, distribuidora, cnh                          | Expedição                     |


