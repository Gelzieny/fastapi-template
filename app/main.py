from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from starlette.responses import RedirectResponse

from app.controller.user_controller import usuario_controller
from app.dependecias.settings import settings

app = FastAPI(
    title="Template API - FastAPI",
    description="""
    Projeto base (template) desenvolvido com FastAPI.  
    Este template fornece estrutura inicial para criação de APIs, incluindo:  
    - Gerenciamento de usuários  
    - Controle de permissões de acesso  
    - Rotas de monitoramento e documentação automática  

    Pode ser utilizado como ponto de partida para novos projetos, garantindo boas práticas e organização.
    """,
    version=settings.APP_VERSION,
    root_path=settings.APP_CONTEXT_PATH if settings.APP_CONTEXT_PATH else ""
)

app.openapi_version = "3.0.2"
app.include_router(usuario_controller)

# --- Rota de Redirecionamento da Raiz para a Documentação ---
@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")

@app.get("/monitor", tags=["Health"])
async def statusaplicacao():
    return True