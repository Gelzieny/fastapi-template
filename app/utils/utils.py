import re
from app.models.perms_model import *

just_numbers = lambda a: ''.join(re.findall("\d+", a))

def mensagem_retorno(self, mensagem, cod_retorno):
    response = PermsResponse(
        mensagem=mensagem, 
        cod_retorno=cod_retorno,
        tipo_retorno='success' if cod_retorno == 0 else 'error',
    )
    return response
