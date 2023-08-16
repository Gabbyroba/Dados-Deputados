# Requisição e Processamento de Despesas dos Deputados Federais 

Este repositório contém um script em Python que faz a requisição e processa dados relacionados às despesas de deputados brasileiros da API da "Câmara dos Deputados". O script utiliza as bibliotecas `requests`, `json` e `pandas` para coletar dados, organizá-los e exportar os resultados processados.

## Pré-requisitos

Antes de executar o script, certifique-se de ter as seguintes bibliotecas instaladas:

- `requests`: Para fazer requisições HTTP à API.
- `json`: Para manipulação de dados JSON.
- `pandas`: Para manipulação e análise de dados.
- `tqdm`: Para exibir barras de progresso.

Você pode instalar essas bibliotecas usando o seguinte comando:

```bash
pip install requests pandas tqdm
```

## Uso

1. Clone este repositório para sua máquina local:

```bash
git clone https://github.com/Gabbyroba/Dados-Deputados.git
```

2. Navegue até o diretório clonado:

```bash
cd Dados-Deputados
```

3. Abra o arquivo de script `main.py` no seu editor ou IDE Python preferido.

4. Execute o script para iniciar a recuperação e o processamento de dados. O script realiza as seguintes etapas:

   - Recupera informações sobre os deputados da API.
   - Recupera as despesas individuais dos deputados com base em seus IDs e organiza os dados.
   - Associa as informações dos deputados às suas respectivas despesas.
   - Processa os dados, remove caracteres indesejados e elimina valores nulos.
   - Exporta os dados limpos e processados para um arquivo do Excel.

5. Após a execução do script, você encontrará dois arquivos do Excel no mesmo diretório:
   - `despesasdep.xlsx`: Os dados brutos com as despesas antes do processamento.
   - `despesasdepfinal.xlsx`: Os dados limpos e processados com as despesas.

## Reconhecimentos

Este script foi criado utilizando as bibliotecas `requests`, `json` e `pandas`, e aproveita a API da "Câmara dos Deputados" para coletar e processar dados relacionados às despesas dos deputados brasileiros. Ele fornece uma base para análises e visualizações de dados futuras.

Para qualquer dúvida, ou problema, entre em contato pelo e-mail [gabbyramosbr2@gmail](mailto:gabbyramosbr2@gmail.com).
