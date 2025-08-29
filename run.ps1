# Ativa o ambiente virtual
.\venv\Scripts\Activate.ps1

# Roda o Uvicorn com FastAPI
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080

# Desativa o ambiente virtual
deactivate
