# Sistema-de-Loja-Virtual - AbraCaxi

O AbraCaxi é um projeto de POO que simula um e-commerce no qual é possível realizar compras de produtos físicos e digitais. No sistema é possível escolher os produtos, adicionar ao carrinho, realizar a compra, confirmar o pagamento, acompanhar a entrega, conferir os produtos mais vendidos e a tabela de valores de frete conforme o cep, gerar relatórios de faturamento diário e mensal, status de pedidos, vendas e outros. O objetivo do projeto é aplicar de forma prática conceitos importantes da programação orientada a objetos empregando conceitos importantes tais como: herança, encapsulamento, validações e composição. As principais tecnologias utilizadas no desenvolvimento do projeto foram: python, como linguagem de programação, sqlite, para a persistência dos dados e FastApi como framework para a criação da API.

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



# Como executar

Para executar o sistema de loja virtual, primeiramente será necessário possuir o python instalado no seu computador em uma versão entre 3.11 e 3.13. Após isso, você deve fazer o download de todos os arquivos do projeto e instalar as bibliotecas presentes no arquivo requirements.txt usando o comando pip install -r requirements.txt. Após a instalação das bibliotecas, para executar o programa usando o FastAPI digite no terminal o comando:  uvicorn main:app --reload  
Depois de inicializar o uvicorn, um link será exibido no terminal

![alt text](image.png)

Você deve copiar esse link e inseri-lo no seu navegador dessa forma

![alt text](image-1.png)

e adicionar /docs para acessar a documentação do FastAPI

![alt text](image-2.png)

Pressione enter e deverá ser exibida essa tela:

![alt text](image-3.png)

Observação importante: Para testar o programa no navegador é necessário manter o terminal com o uvicorn aberto fazer manter a conexão.

Para realizar as operações basta clicar na seta para baixo representada no exemplo 

![alt text](image-4.png)

Essa aba será aberta

![alt text](image-5.png)
Depois clique em Try it out e edite as informações de cada atributo 

![alt text](image-6.png)

Agora clique em Execute. Se aparecer 200 como resposta como nesse caso:

![alt text](image-7.png)

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