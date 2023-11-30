from typing import ClassVar
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta


class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://admin:admin@localhost:5432/faculdade"
    DBBaseModel: ClassVar[DeclarativeMeta] = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()