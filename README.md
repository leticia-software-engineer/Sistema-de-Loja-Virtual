# Sistema-de-Loja-Virtual - Definicão e objetivos.

O AbraCaxi é um projeto de POO que simula um e-commerce no qual é possível realizar compras de produtos físicos e digitais. No sistema é possível escolher os produtos, adicionar ao carrinho, realizar a compra, confirmar o pagamento, acompanhar a entrega, conferir os produtos mais vendidos e a tabela de valores de frete conforme o cep, gerar relatórios de faturamento diário e mensal, status de pedidos, vendas e outros. O objetivo do projeto é aplicar de forma prática conceitos importantes da programação orientada a objetos empregando conceitos importantes tais como: herança, encapsulamento, validações e composição. As principais tecnologias utilizadas no desenvolvimento do projeto foram: python, como linguagem de programação, sqlite, para a persistência dos dados e FastApi como framework para a criação da API.

# Uma breve explicação do código


# Estrutura 

loja virtual/
├── api/<br>
│   ├── rotas/<br>
│   │   ├── rotas_cliente.py<br>
│   │   ├── rotas_frete.py<br>
│   │   ├── rotas_pagamento.py<br>
│   │   ├── rotas_pedido.py<br>
│   │   ├── rotas_produto_digital.py<br>
│   │   ├── rotas_produto_fisico.py<br>
│   │   ├── rotas_relatorios.py<br>
│   │   ├── rotascarrinho.py<br>
|   │   └── rotasconfig.py<br>
|<br>
├── data/<br>
│   ├──ceps_cotacoes_ceara.json<br>
│   └── sqlite.py<br>
|<br>
├── Fonte/<br>
│   ├── cancelamento_pedido.py<br>
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
├── teste/<br>
│   ├── test_carrinho.py<br>
│   ├── test_cliente.py<br>
│   ├── test_pedido.py<br>
│   └── test_produto_digital.py<br>
|
├── Utilitarios/<br>
│   ├── LICENSE <br>
│   └── instancias de teste.txt<br>
|<br>
├── loja virtual.db<br>
├── main.py<br>
├── pytest.ini<br>
├── README.md<br>
├── relatorio de pedidos por status.json<br>
├── relatorio por cep.json<br>
├── relatorio faturamento.json<br>
└── requirements.txt<br>

# UML Textual

| **CLASSE**         | **MÉTODOS**                                                                                      | **ATRIBUTOS**                                                   | **RELACIONAMENTOS** |
|--------------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|---------------------|
| CancelamentoPedido | __init__, cancelar                                                                               | confirmar, id_do_carrinho, confirma_cep, num_pedido             | Herda de Pedido     |
| Carrinho           | __init__, adicionarcarrinho, visualizarcarrinho, excluircarrinho, __len__                        | cpf, codigo_produto, quantidade, com_frete                      |                     |
| Cliente            | __init__, getters e setters, CRUD                                                                | nome_cliente, email, cpf, rua, cep                              |                     |
| Configuracoes      | tabela_frete, politica_de_cancelamento, orientacoes_da_aplicacao                                 |                                                                 |                     |
| Expedicao          | __init__, marcar_envio, marcar_entregue                                                          | cod_entrega                                                     |                     |
| Frete              | __init__, verificar_valor_frete                                                                  | cep                                                             |                     |
| Pagamentos         | __init__, registrar_pagamento, alterar_status_pedido, atualizar_estoque                          | num_pedido, forma_pagamento, valor_pago, status, data_pagamento |                     |
| Pedido             | __init__, calcular_subtotal_com_frete, calcular_subtotal, fechar_pedido, visualizar_meus_pedidos | confirmar, id_do_carrinho, confirma_cep                         |                     |
| ProdutoFisico      | __init__, CRUD                                                                                   |  nome, codigo, categoria, preco_unitario, estoque, frete        | Herda de Produto    |
| ProdutoDigital     | __init__, CRUD                                                                                   | nome, codigo, categoria, preco_unitario, estoque                | Herda de Produto    |
| Produto            | __init__, getters e setters                                                                      |  nome, codigo, categoria, preco_unitario, estoque               |                     |
| Relatorios         | __init__, faturamento_periodo, pedidos_por_cep, pedidos_por_status                               | data_relatorio                                                  |                     |


# Como executar

Para executar o sistema de loja virtual, primeiramente será necessário possuir o python instalado no seu computador em uma versão entre 3.11 e 3.13. Após isso, você deve fazer o download de todos os arquivos do projeto e instalar as bibliotecas presentes no arquivo requirements.txt usando o comando pip install -r requirements.txt. Após a instalação das bibliotecas, para executar o programa usando o FastAPI digite no terminal o comando:  uvicorn main:app --reload  
Depois de inicializar o uvicorn, um link será exibido no terminal

<img width="1087" height="192" alt="image" src="https://github.com/user-attachments/assets/6bb5d189-de90-4232-9203-b0a431499b7c" />

Você deve copiar esse link e inseri-lo no seu navegador dessa forma

<img width="407" height="126" alt="image" src="https://github.com/user-attachments/assets/dfacec25-a919-402d-b5c0-2ea4d3820ab8" />

e adicionar /docs para acessar a documentação do FastAPI

<img width="452" height="117" alt="image" src="https://github.com/user-attachments/assets/91f7995b-2cc1-473f-a26f-b1126df6a872" />

Pressione enter e deverá ser exibida essa tela:

<img width="1875" height="908" alt="image" src="https://github.com/user-attachments/assets/05b46281-d236-492e-a820-43e92353cb93" />

Observação importante: Para testar o programa no navegador é necessário manter o terminal com o uvicorn aberto fazer manter a conexão.

Para realizar as operações basta clicar na seta para baixo representada no exemplo 

<img width="1815" height="82" alt="image" src="https://github.com/user-attachments/assets/0bb8731c-8f21-40e6-b014-a17001360492" />

Essa aba será aberta

<img width="1801" height="487" alt="image" src="https://github.com/user-attachments/assets/3a7bf36d-1bca-4b80-af31-038d898b0003" />

Depois clique em Try it out e edite as informações de cada atributo 

<img width="1780" height="517" alt="image" src="https://github.com/user-attachments/assets/33ab2a3c-13da-4083-b611-9bd43568cf66" />

Agora clique em Execute. Se aparecer 200 como resposta como nesse caso:

<img width="1751" height="433" alt="image" src="https://github.com/user-attachments/assets/f548eefe-0f3d-46ef-805b-6a03b368aa69" />

O programa foi executado com sucesso.

Caso você digite alguma informação inválida com valores não condizentes aos solicitados como int no lugar de string ou dados de tamanho inferior ao solicitado será exibido o número 422 que indica que as informações não puderam ser processadas pelo servidor por serem inválidas.

Além disso, também existem alguns testes na pasta testes que utilizam a biblioteca pytest. Para executá-los você deve digitar no terminal o comando: pytest testes/nomedoarquivo.py 

# Algumas instâncias para usar como teste

Intâncias de Cliente

{
  "nome": "Letícia",
  "email": "leticia@gmail.com",
  "cpf": "12312312345",
  "rua": "José Feitosa",
  "cep": "63260000"
}

{
  "nome": "Laura",
  "email": "laura@gmail.com",
  "cpf": "20212345612",
  "rua": "Avenida Velha",
  "cep": "63240000"
}

{
  "nome": "Júlia",
  "email": "julia@gmail.com",
  "cpf": "34581049234",
  "rua": "Bela Vista",
  "cep": "63210000"
}

Intâncias de produto físico

{
  "nome": "copo",
  "cod": 1,
  "categoria": "utensilios",
  "preco": 3,
  "estoque": 3,
  "frete": "sim"
}

{
  "nome": "tijela",
  "cod": 2,
  "categoria": "utensilios",
  "preco": 70,
  "estoque": 60,
  "frete": "sim"
}

{
  "nome": "garrafa",
  "cod": 3,
  "categoria": "utensilios",
  "preco": 50,
  "estoque": 60,
  "frete": "sim"
}

Intâncias produto digital

{
  "nome": "Ebook O pequeno príncipe",
  "cod": 4,
  "categoria": "livro digital",
  "preco": 20,
  "estoque": 100
}

{
  "nome": "Ebook O arco-íris do meu ser",
  "cod": 5,
  "categoria": "livro digital",
  "preco": 30,
  "estoque": 100
}

Intâncias de carrinho

{
  "cpf": "34581049234",
  "codigo_produto": 2,
  "quantidade": 2,
  "com_frete": "sim"
}

{
  "cpf": "34581049234",
  "codigo_produto": 3,
  "quantidade": 1,
  "com_frete": "sim"
}

Instâncias de pedido

{
  "confirmar": "sim",
  "confirme_cpf": "34581049234",
  "confirma_cep": "63210000"
}

Para cancelamento de pedido

{
  "confirmar": "sim",
  "cpf": "34581049234",
  "confirma_cep": "63210000",
  "num_pedido": #Veja o pedido primeiro para saber qual seu id
}

Instâncias de pagamento 

{
  "num_pedido": #informe o número do pedido,
  "forma_pagamento": "pix",
  "valor_pago": 30,
  "status": "pago"
}

Ceps disponíveis para teste

63210000     
63260000     
63240000     
63136000     
63137000     
63180000     
63138000     
63139000     
63510000     
63511000     
63512000     
63010900     
63010905     
63250000     
63255000     
63165000     

Para marcar envio cole o código gerado no momento do fechamento do pedido com frete após a confirmação do pagamento

Os relatórios não contêm parâmetros basta clicar em try it out e em execute que eles são gerados ou atualizados no arquivo json correspondente.

As configurações também não têm parâmetros mas podem ser visualizadas usando o mesmo comando só que diretamente na documentação do FastAPI