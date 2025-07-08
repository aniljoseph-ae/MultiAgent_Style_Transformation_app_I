from pydantic_settings import BaseSettings
from pydantic import Field, AliasChoices

class Settings(BaseSettings):
    ultrasafe_api_key: str = Field(..., validation_alias=AliasChoices("ULTRASAFE_API_KEY"))
    ultrasafe_base_url: str = Field("https://api.us.inc/usf/v1/", validation_alias=AliasChoices("ULTRASAFE_BASE_URL"))
    chroma_db_path: str = Field("./chroma_db", validation_alias=AliasChoices("CHROMA_DB_PATH"))
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

def get_settings():
    """Singleton settings instance"""
    return Settings()