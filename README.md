📁 **LabTrans - Segunda Fase**

## Descrição do Projeto

O projeto consiste em uma estrutura backend utilizando Python (Peewee) e Sqlite para receber e manipular dados de um levantamento de uma rodovia extraídos utilizando visão computacional.

### Pré-requisitos

- Conda (versão 4.12.0)
- SQLite (versão 3.41.2)

### Configuração do Ambiente

1. Crie um ambiente virtual com Conda:

   ```shell
   conda create --name peewee_env python=3.9
   ```

2. Ative o ambiente virtual:

   ```shell
   conda activate peewee_env
   ```

3. Instale as dependências do projeto:

   ```shell
   pip install -r requirements.txt
   ```

### Configuração do Banco de Dados

1. Execute o arquivo `init.sql` para configurar o banco de dados SQLite:

   ```shell
   sqlite3 labtrans.db < init.sql
   ```

### Executando o Projeto

1. Execute o arquivo principal:

   ```shell
   python VideoInsights.py
   ```
1. Executar a API:

   ```shell
   python VideoInsightsAPI.py
   ```

