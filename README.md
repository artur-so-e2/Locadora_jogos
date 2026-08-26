# Locadora de jogos

Uma locadora trabalha com jogos para diferentes plataformas, como PlayStation, Xbox e Nintendo Switch.

Cada **Jogo** possui um título, uma plataforma, um gênero e um valor de locação por dia.

A locadora também mantém o cadastro de seus **Clientes**. Cada cliente possui nome e telefone.

Quando um cliente realiza uma locação, o sistema deve registrar o jogo escolhido, a quantidade de dias e calcular o valor total.

A locadora oferece descontos de acordo com o período da locação:

- Até 3 dias: sem desconto.
- Acima de 3 dias: 5% de desconto.
- Acima de 7 dias: 10% de desconto.
O desconto deve ser aplicado sobre o valor total da locação.

**Exemplo**

Considere um jogo cujo valor da diária seja **R$ 10,00**.

Se o cliente alugá-lo por 5 dias:

**Valor sem desconto:**

5 × R$ 10,00 = R$ 50,00

**Desconto:**

5% de R$ 50,00 = R$ 2,50

**Valor final:**

R$ 47,50

**Requisitos**

Desenvolva uma aplicação em Python que permita:

1. Cadastrar jogos.
2. Listar os jogos cadastrados.
3. Cadastrar clientes.
4. Listar os clientes cadastrados.
5. Realizar uma locação.
6. Calcular automaticamente o desconto e o valor final.
7. Listar as locações realizadas.
   
O programa deve utilizar:

- Funções;
- Parâmetros;
- Listas;
- Dicionários;
- Estruturas de decisão;
- Estruturas de repetição;
- Arquivos JSON;
- Organização do programa em mais de um arquivo.
- Persistência dos dados

Os dados devem ser armazenados em três arquivos diferentes:

jogos.json – cadastro dos jogos;
clientes.json – cadastro dos clientes;
locacoes.json – histórico das locações.
Ao iniciar o programa, os dados existentes nos arquivos JSON devem ser carregados.

Sempre que um novo jogo, cliente ou locação for cadastrado, os dados correspondentes devem ser atualizados no respectivo arquivo JSON.

**Sugestão de organização**

O projeto pode ser organizado da seguinte forma:

Locadora_jogos

├── main.py

├── jogos.py

├── clientes.py

├── locacoes.py

├── persistencia.py

├── jogos.json

├── clientes.json

└── locacoes.json

**Desafio adicional:** inclua no cadastro de cada jogo a quantidade de cópias disponíveis. Uma locação somente poderá ser realizada se houver pelo menos uma cópia disponível. Ao realizar a locação, a quantidade disponível deverá ser reduzida em uma unidade.
