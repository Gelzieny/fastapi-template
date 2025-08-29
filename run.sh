#!/bin/bash
cd /repositorio-projeto
source venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8080 --log-level debug --reload
deactivate
