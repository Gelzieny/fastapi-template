# 🚀 FastAPI Project Template


Este repositório é um template `base para projetos FastAPI`, já estruturado com boas práticas, conexão com banco de dados (PostgreSQL via SQLAlchemy), versionamento de API e suporte a variáveis de ambiente.


📂 Estrutura do Projeto


````bash
fastapi_project/
│── app/
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/
│   │           └── users.py
│   ├── core/
│   │   └── config.py
│   ├── db/
│   │   ├── base.py
│   │   └── session.py
│   ├── models/
│   │   └── user.py
│   ├── schemas/
│   │   └── user.py
│   ├── main.py
│   └── __init__.py
│
├── tests/
│   └── test_users.py
│
├── .env
├── requirements.txt
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
git clone https://github.com/seuusuario/fastapi-template.git
cd fastapi-template



### 🍏 MacOS & 🐧 Linux (Ubuntu/Debian/Fedora/etc.)
````bash
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

#Iniciando servidor
python3 manage.py
````

### 🪟 Windows
````bash
python3 -m venv venv && venv\Scripts\activate && pip install -r requirements.txt

#Iniciando servidor
python manage.py
````
