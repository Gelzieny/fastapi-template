# 🚀 FastAPI Project Template


Este repositório é um template `base para projetos FastAPI`, já estruturado com boas práticas, conexão com banco de dados (PostgreSQL via SQLAlchemy), versionamento de API e suporte a variáveis de ambiente.


📂 Estrutura do Projeto


````bash
fastapi_project/
│── app/
│   ├── controller/
│   │   └── user_controller.py
│   ├── utils/
│   │   └── utils.py
│   ├── dependecias/
│   │   ├── conexao_postgres.py
│   │   └── security.py
│   │   └── settings.py
│   ├── models/
│   │   └── perms_model.py
│   │   └── user_model.py
│   ├── repository/
│   │   └── usuario_repository.py
│   ├── main.py
│
├── .env
├── .env-exemplo
├── .gitignore
├── requirements.txt
├── docker-compose.yml
├── run2.sh     # Produção
├── run.sh      # Linux / MacOS
├── run.bat     # Windows (CMD)
├── run.ps1     # Windows (PowerShell)
└── README.md
````

## ⚙️ Requisitos
- [Python 3.11+](https://www.python.org/downloads/)  
- [PostgreSQL](https://www.postgresql.org/) (ou usar Docker)  


## 📦 Instalação

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/Gelzieny/fastapi-template.git
cd fastapi-template
```

### Criar ambiente virtual


#### 🍏 MacOS & 🐧 Linux (Ubuntu/Debian/Fedora/etc.)
````bash
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

#Iniciando servidor
python3 manage.py
````

#### 🪟 Windows
````bash
python3 -m venv venv && venv\Scripts\activate && pip install -r requirements.txt

#Iniciando servidor
python manage.py
````

## 🛠️ Configuração

Edite o arquivo .env para configurar o banco de dados:

````bash
POSTGRES_USER=postgres
POSTGRES_PASSWORD=123
POSTGRES_DB=meu_banco
POSTGRES_SERVER=localhost
POSTGRES_PORT=5432
````

## ▶️ Executando o projeto

````bash

# Rodar o projeto em produção:
$ ./run2.sh

# Linux / MacOS:
$ ./run.sh

# Windows (CMD):
$ run.bat

# Windows (PowerShell):
$ .\run.ps1
````
Servidor rodará em:
👉 [http://localhost:8080](http://localhost:8080)  


## 📚 Documentação da API

FastAPI gera a documentação automaticamente:

* [Swagger UI:](http://localhost:8080/docs)
* [Redoc:](http://localhost:8080/redoc)

## 🧪 Testes
Rodar testes com `pytest`:

````bash
$ pytest -v
````

🚀 Futuras melhorias

* Integração com Docker + Docker Compose
* Migrações automáticas com Alembic
* Autenticação com JWT / OAuth2
* CI/CD com GitHub Actions / GitLab CI