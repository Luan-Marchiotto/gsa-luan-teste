# Projeto proposto GSA

<p align="center">
  <img src="static/img/logo.jpg" 
       alt="Logo da GSA" 
       width="150" 
       style="border-radius: 50%; border: 3px solid #333;" />
</p>


### 🏫 SchoolManager - Sistema de Gerenciamento Escolar
- Este projeto é uma aplicação web chamada "SchoolManager", desenvolvida com Python e Django, permitindo o cadastro e listagem de alunos e salas de aula.

## 🛠️ Tecnologias usadas

- Python 3.12 + [Python](https://www.python.org/downloads/ "Site oficial do Python")
- PostgreSQL [PostgreSQL](https://www.postgresql.org/download/ "Site oficial do PostgreSQL")
- Django 6
- HTML, CSS
- Git (para controle de versão)

## ⚠️ Pré-requisitos

- Antes de rodar o projeto, certifique-se de:

- Ter Python 3.12 instalado.

- Ter PostgreSQL instalado e configurado.

- Sempre ativar o ambiente virtual (venv) antes de instalar dependências ou rodar o servidor.

## 🏗️ Estrutura do projeto

```bash
GSAteste/

├── alunos/ # App para gerenciamento dos alunos.
├── core/ # App para receber informações.
├── escola/ # Configurações do django.
├── salas/ # App para gerenciamento das salas.
├── static/
├── templates/ 
│ └── base.html # Template base
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt # Lista de dependências do projeto
```

## Passo 1: Clonar o projeto.
```bash
git clone https://github.com/Luan-Marchiotto/gsa-luan-teste.git
cd gsa-luan-teste
```

## Passo 2: Criar e ativar o ambiente virtual (venv).

- Criar o ambiente virtual
    ```bash
    python -m venv venv
    ```
- Ativando o ambiente virtual

    **Windows:**
    ```bash
    .\venv\Scripts\activate
    ```

    **Linux/ macOS:**
    ```bash
     source venv/bin/activate
    ```

## Passo 3: Instalar dependências.
```bash
pip install -r requirements.txt
```

## Passo 4: Configurando o PostgreSQL.
- Criação do Banco de Dados no terminal (`psql`) ou o pgAdmin.
    ```bash
    psql -U postgres
    ```

- 4.1 Prompt no PostgreSQL
    - 4.1.1 Criação do banco
    
    ```sql
    CREATE DATABASE nome_do_banco;
    ```
    - Substitua `nome_do_banco` pelo nome que quer para o banco, exemplo `escola_db`.

    <br>

    - 4.1.2 Criar um usuário (se necessário)

    ```sql
    CREATE USER seu_usuario WITH PASSWORD 'sua_senha';
    ```
    - Substitua `sua_senha` pela senha de acesso do usário ou do pgAdmin, exemplo: `senha123`

    <br>

    - 4.1.3 Dar privilégios ao usuário

    ```sql
    GRANT ALL PRIVILEGES ON DATABASE nome_do_banco TO seu_usuario;
    ```
    - Substitua `nome_do_banco` e `seu_usuario`.

## Passo 5: Criar arquivo `.env`.
- Na raiz do projeto, crie um arquivo chamado `.env` com o conteúdo:
```bash
DEBUG = True 
DB_NAME =  "nome_do_banco"
DB_USER = "seu_usuario"
DB_PASSWORD = "sua_senha"
DB_HOST = localhost
DB_PORT = 5432 # Porta padrão de instalação do PostgreSQL
```
💡 Dica: Ajuste os valores conforme o banco de dados criado no passo anterior.

## Passo 6: Rodar o servidor.
### Rodar migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Iniciar o servidor
- No terminar, execute:
```bash
python .\manage.py runserver
```
- Acessar o sistema:
```bash
Abra no navegador: "http://127.0.0.1:8000/"  # Porta padrão de inicialização
```

# 💡 Observações

- O projeto foi desenvolvido utilizando VSCode, mas você pode usar qualquer editor de sua preferência.

- DEBUG = True deve ser usado apenas em desenvolvimento. Para produção, ajuste para False.

- Certifique-se de rodar o banco de dados e migrations antes de acessar qualquer página.
