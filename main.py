import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Carregar o arquivo de despesas em um DataFrame
df_despesas = pd.read_excel('despesasdepfinal.xlsx')
tabela = df_despesas
dfr_despesas = pd.read_excel('despesasdepfinalcopia.xlsx')
tabela2 = dfr_despesas

# Armazenar o dataframe em uma variável 
dftree = pd.DataFrame(tabela)
df = dftree

# Exibir informações estatísticas do DataFrame
tabela.describe()

# Filtrar despesas com valores negativos
valores_negativos = tabela[tabela['valorLiquido'] < 0]

# Remover linhas específicas do DataFrame
tabela = tabela.drop(12636, axis='index')
tabela = tabela.drop(23040, axis='index')
tabela = tabela.drop(32069, axis='index')
tabela = tabela.drop(33479, axis='index')

# Plotar o gráfico de barras dos gastos por partido
plt.bar(tabela['siglaPartido'], tabela['valorLiquido'])
plt.xlabel('siglaPartido')
plt.ylabel('valorLiquido')
plt.title('Gastos por Partido')
plt.xticks(rotation=90)
plt.show()

# Agrupar as despesas por categoria e somar os valores
agrupadas = tabela[['tipoDespesa', 'valorLiquido']].groupby('tipoDespesa').sum()

# Truncar os nomes das despesas
agrupadas.index = [despesa[:10] + '...' if len(despesa) > 10 else despesa for despesa in agrupadas.index]

# Plotar o gráfico de barras das despesas por categoria
agrupadas.plot(kind='bar')

# Configurar o título e os rótulos dos eixos
plt.title('Despesas por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Valor Total')

# Rotacionar os rótulos das categorias
plt.xticks(rotation=45)

# Exibir o gráfico
plt.show()

# Plotar o histograma interativo dos gastos por sigla de partido usando Plotly
fig = px.histogram(tabela, x='siglaPartido', color='siglaPartido')
fig.show()

# Salvar o histograma interativo como um arquivo HTML
fig.write_html('histogramainterativo.html')

# Agrupar as despesas por tipo e somar os valores
dados = tabela[['tipoDespesa', 'valorLiquido']].groupby('tipoDespesa').sum().reset_index()

# Ordenar os dados pelo valorLiquido de forma decrescente
dados = dados.sort_values('valorLiquido', ascending=False)

# Criar o gráfico de barras horizontais
fig3 = go.Figure(data=go.Bar(
    x=dados['valorLiquido'],
    y=dados['tipoDespesa'],
    orientation='h',
))

# Configurar o layout do gráfico de barras horizontais
fig3.update_layout(
    title='Despesas por Tipo',
    xaxis_title='Valor Total',
    yaxis_title='Tipo de Despesa',
    xaxis_range=[0, max(dados['valorLiquido'])]  # Definir o intervalo do eixo x com base no valor máximo
)

# Exibir o gráfico de barras horizontais
fig3.show()

# Calcular a contagem de ocorrência de cada siglaUF
counts = df['siglaUF'].value_counts()

# Criar um DataFrame com as informações
df_treemap = pd.DataFrame({'siglaUF': counts.index, 'count': counts.values, 'valorLiquido': counts.values})

# Criar o treemap
fig2 = go.Figure(go.Treemap(
    labels=df_treemap['siglaUF'],
    parents=[""] * len(df_treemap),  # Define todos os nós raiz
    values=df_treemap['valorLiquido'],
    text=df_treemap['valorLiquido'].apply(lambda x: f"R${x:.2f}"),  # Adiciona o prefixo "R$" e formata com duas casas decimais
    textposition="middle center",  # Define a posição do texto no centro da área
    hovertemplate='<b>%{label}</b> <br> Valor: %{text}',
))

# Configurar o título
fig2.update_layout(title='Gastos por UF')

# Exibir o gráfico
fig2.show()

# Criar o gráfico de histograma por tipo de despesa
fig4 = px.histogram(tabela2, x='tipoDespesa', color='tipoDespesa')

# Exibir o gráfico
fig4.show()