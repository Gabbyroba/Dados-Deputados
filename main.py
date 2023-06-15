from tqdm import tqdm
import requests
import json 
import pandas as pd 

# PRIMEIRA REQUISIÇÃO - DADOS DOS DEPUTADOS 
url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome'
r = requests.get(url, allow_redirects=True)
data = r.json()
deputados = data['dados']
dfr = pd.DataFrame(deputados)

# CRIA LISTAS VAZIAS PARA ARMAZENAR OS DADOS
despesas_totais = []
listas2 = []
listas3 = []
listas4 = []
listas5 = []
listas6 = []
listas7 = []

# DESPESAS INDIVIDUAIS DE DEPUTADOS POR ID
for id_deputado in tqdm(deputados, desc='Progresso'):
    id_deputado = id_deputado['id']
    page = 1
    has_next_page = True

    # SEGUNDA REQUISIÇÃO - PAGINAÇÃO E BUSCA DE DESPESAS TOTAIS POR ID  
    while has_next_page:
        des = f'https://dadosabertos.camara.leg.br/api/v2/deputados/{id_deputado}/despesas?ano=2023&itens=100&pagina={page}'
        req = requests.get(des, allow_redirects=True)
        dado = req.json()
        despesas = dado['dados']
        despesas_totais.extend(despesas)
        
        # ARMAZENA DADOS NAS LISTAS
        for c in range (1, len(despesas)):    
            nome = dfr.loc[dfr['id'] == id_deputado, 'nome']
            sigla_partido = dfr.loc[dfr['id'] == id_deputado, 'siglaPartido']
            sigla_Uf = dfr.loc[dfr['id'] == id_deputado, 'siglaUf']
            id_Legislatura = dfr.loc[dfr['id'] == id_deputado, 'idLegislatura']
            url_Foto = dfr.loc[dfr['id'] == id_deputado, 'urlFoto']
            email = dfr.loc[dfr['id'] == id_deputado, 'email']

            listas2.append(nome.tolist())
            listas3.append(sigla_partido.tolist())
            listas4.append(sigla_Uf.tolist())
            listas5.append(id_Legislatura.tolist())
            listas6.append(url_Foto.tolist())
            listas7.append(email.tolist())
        
        # PERCORRE AS PÁGINAS E ADICIONA + 1, CASO TENHA LINK DE "NEXT PAGE"
        if 'next' in dado['links']:
            page += 1
        else:
            has_next_page = False

# JUNTA AS LISTAS  
zipado = list(zip(listas2, listas3, listas4, listas5, listas6, listas7))

# CRIA OS DATAFRAMES
dfdep = pd.DataFrame(zipado)
dfdesp = pd.DataFrame(despesas_totais)

# RENOMEIA COLUNAS DO DATAFRAME DFDEP
dfdep.rename(columns={0: 'nome', 1: 'siglaPartido', 2: 'siglaUF', 
                      3: 'idLegislatura', 4: 'foto', 5: 'email'}, inplace=True)

# RELACIONA OS DATAFRAMES E EXPORTA COMO XLSX (EXCEL)
dffinal = dfdep.join(dfdesp)
dffinal.to_excel('despesasdep.xlsx')

# LÊ A TABELA PARA TRATAR DADOS
despesasxcel = pd.read_excel('despesasdep.xlsx')
tabela = despesasxcel

# ELIMINA CARACTERES INDESEJADOS
tabela['nome'] = tabela['nome'].str.strip("[]'")
tabela['siglaPartido'] = tabela['siglaPartido'].str.strip("[]'")
tabela['siglaUF'] = tabela['siglaUF'].str.strip("[]'")
tabela['idLegislatura'] = tabela['idLegislatura'].str.strip("[]'")
tabela['foto'] = tabela['foto'].str.strip("[]'")
tabela['email'] = tabela['email'].str.strip("[]'")

# ELIMINA VALORES NULOS E COLUNAS DESNECESSÁRIAS
tabela = tabela.dropna()
tabelaf = tabela.drop(columns='Unnamed: 0')

# SALVA O ARQUIVO FINAL EM XLSX (EXCEL) IGNORANDO O INDEX:
tabelaf.to_excel('despesasdepfinal.xlsx', index=False)
