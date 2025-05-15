Este projeto tem como objetivo realizar uma análise exploratória de dados de vendas a partir de um arquivo .csv, utilizando Python, pandas, matplotlib e seaborn. Ao longo do processo, extraímos insights comerciais relevantes por meio de agrupamentos, cálculos e visualizações gráficas.

🧰 Tecnologias Utilizadas
Python 3

pandas

matplotlib

seaborn

🗂️ Dados Utilizados
O arquivo vendas.csv simula registros de vendas com as seguintes colunas:

Data – data da venda

ID Pedido – código identificador da venda

Produto – nome do item vendido

Categoria – tipo de produto

Quantidade – unidades vendidas

Preço Unitário – valor por unidade

Total – valor da venda (calculado)

Vendedor – responsável pela venda

🔍 Etapas da Análise
✔️ 1. Carregamento e limpeza
Leitura do arquivo .csv

Conversão da coluna Data para o formato datetime

Criação de nova coluna ano_mes (ex: 2025-05)

📊 2. Análises realizadas
Faturamento por categoria

Produtos mais vendidos

Tendência de vendas por mês

Desempenho por vendedor

Cálculo do ticket médio

📈 3. Visualizações
Gráficos de barras horizontais

Gráfico de linha (vendas mensais)

Gráfico de pizza (opcional)

Paleta de cores com seaborn

💡 Exemplos de Insights
Quais categorias vendem mais?

Qual produto tem maior volume de vendas?

Quais meses são mais lucrativos?

Quem são os melhores vendedores?

Qual é o valor médio por pedido?

🧠 Aprendizados
Este projeto reforça o uso de:

Agrupamentos e somatórios com groupby()

Manipulação de datas com .dt

Criação de novas colunas derivadas

Visualizações com matplotlib e seaborn

Geração de insights práticos a partir de dados reais
