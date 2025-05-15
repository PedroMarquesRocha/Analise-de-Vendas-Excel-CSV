import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Carregando os dados

df = pd.read_csv('vendas_ficticias.csv')

print(df)

df['Data'] = pd.to_datetime(df['Data'], errors='coerce')
df['Data_formatada'] = df['Data'].dt.strftime('%d/%m/%Y')
df['Data'].fillna(pd.Timestamp('1900-01-01'), inplace=True)

# Faturamento por categoria
categoria_total = df.groupby('Categoria')['Total'].sum().sort_values(ascending=False)

# Produto mais vendido (por quantidade)
produto_total = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)

# Vendas por mês

df['mes'] = df['Data'].dt.month
vendas_por_mes = df.groupby('mes')['Total'].sum().sort_values()
print(vendas_por_mes)

# Calcular o ticket médio

agrupado = df.groupby('Categoria')[['Total', 'Quantidade']].sum()
agrupado['Ticket Médio'] = agrupado['Total'] / agrupado['Quantidade']
ticket_medio = agrupado[['Ticket Médio']].sort_values(by='Ticket Médio', ascending=False)
print(ticket_medio)

# Desempenho por vendedor

vendas_por_vendedor = df.groupby('Vendedor')['Total'].sum().sort_values(ascending=False)
print(vendas_por_vendedor)

# Visualizações

# Visualização de Participação por Categoria
categoria_total = df.groupby('Categoria')['Total'].sum().sort_values(ascending=False)
plt.figure(figsize=(7, 7))
plt.pie(categoria_total, labels=categoria_total.index, autopct='%1.1f%%', startangle=140)
plt.title('Participação de Faturamento por Categoria')
plt.tight_layout()
plt.savefig('participacao_por_categoria.png')
plt.show()

# Visualização de Evolução temporal de vendas
df['ano_mes'] = df['Data'].dt.to_period('M').astype(str)
vendas_mensais = df.groupby('ano_mes')['Total'].sum().reset_index()

plt.figure(figsize=(10, 5))
sns.lineplot(data=vendas_mensais, x='ano_mes', y='Total', marker='o')
plt.title('Vendas por Mês')
plt.xlabel('Ano/Mês')
plt.ylabel('Total Vendido')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('vendas_por_mes.png')
plt.show()

# Visualização de Vendas por mês e categoria
df['mes'] = df['Data'].dt.strftime('%b')
heatmap_data = df.pivot_table(index='Categoria', columns='mes', values='Total', aggfunc='sum', fill_value=0)

plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=True, fmt='.0f', cmap='YlGnBu')
plt.title('Heatmap - Vendas por Categoria e Mês')
plt.xlabel('Mês')
plt.ylabel('Categoria')
plt.tight_layout()
plt.savefig('heatmap_vendas_categoria_mes.png')
plt.show()

# Visualização de Faturamento por Categoria
plt.figure(figsize=(8, 5))
sns.barplot(x=categoria_total.values, y=categoria_total.index)
plt.title('Faturamento por Categoria')
plt.xlabel('Total Vendido')
plt.ylabel('Categoria')
plt.tight_layout()
plt.savefig('faturamento_por_categoria.png')
plt.show()


# Visualização de Produto mais vendido (Quantidade)
produto_total = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=True)
plt.figure(figsize=(8, 8))
produto_total.plot(kind='barh', color='skyblue')
plt.title('Produto mais Vendido (Quantidade)')
plt.xlabel('Quantidade Vendida')
plt.ylabel('Produto')
plt.tight_layout()
plt.savefig('produto_mais_vendido.png')
plt.show()

# Visualização de Ticket médio por categoria
agrupado = df.groupby('Categoria')[['Total', 'Quantidade']].sum()
agrupado['Ticket Médio'] = agrupado['Total'] / agrupado['Quantidade']
ticket_medio = agrupado['Ticket Médio'].sort_values(ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(x=ticket_medio.values, y=ticket_medio.index)
plt.title('Ticket Médio por Categoria')
plt.xlabel('Ticket Médio')
plt.ylabel('Categoria')
plt.tight_layout()
plt.savefig('ticket_medio_por_categoria.png')
plt.show()

# Visualização de Desempenho por Vendedor
vendas_vendedor = df.groupby('Vendedor')['Total'].sum().sort_values(ascending=True)
plt.figure(figsize=(8, 6))
vendas_vendedor.plot(kind='barh', color='lightgreen')
plt.title('Desempenho por Vendedor')
plt.xlabel('Total Vendido')
plt.ylabel('Vendedor')
plt.tight_layout()
plt.savefig('desempenho_por_vendedor.png')
plt.show()
