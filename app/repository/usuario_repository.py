from fastapi import HTTPException
from fastapi.responses import JSONResponse 

from App.utils.utils import *
from App.dependencias.database import ConexaoPostgres

class UsuarioRepository:
    
    def __init__(self, db_connection: ConexaoPostgres):
        self.base = db_connection

    def get_usuarios(self, user: dict) -> dict:
        try:
            pass

        except ValueError as ve:
            return {'error': f"Erro de validação: {str(ve)}"}
        except Exception as e:
            return {'error': f"Erro ao executar a query: {str(e)}"}

    def cadastra_usuario(self, info: dict) -> dict:
        pass

    def deletar_usuario(self, info: dict) -> dict:
        pass