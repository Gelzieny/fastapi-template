from typing import Optional
from pydantic import BaseModel, Field

class Usuarios(BaseModel): 
    nome_usuario: Optional[str] = Field(None, description="Nome do usuário ", example="Teste")
    page: str = Field()
    page_size: str = Field()

class UsuarioCad(BaseModel):
    nome_usuario: str = Field(..., description="Nome do usuário", example="Teste")
    email: str = Field(..., description="E-mail usuário", example="teste@gmail.com")
    senha_usuario: str = Field(..., description="Senha usuário", example="12356fhhgh@#")
  