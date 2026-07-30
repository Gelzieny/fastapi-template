from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')
    
    APP_CONTEXT_PATH: str
    APP_VERSION: str

    POSTGRES_PRODUCAO_DB: str
    POSTGRES_PRODUCAO_USER: str
    POSTGRES_PRODUCAO_HOST: str
    POSTGRES_PRODUCAO_PORT: int
    POSTGRES_PRODUCAO_PASSWORD: str
    
    DATABASE_URL =  f'postgresql://{POSTGRES_PRODUCAO_USER}:{POSTGRES_PRODUCAO_PASSWORD}@{POSTGRES_PRODUCAO_HOST}:{POSTGRES_PRODUCAO_PORT}/{POSTGRES_PRODUCAO_DB}'
        
settings = Settings()