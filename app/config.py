from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str 
    version: str 
    environment: str 
    logging_level: str 
    status: str
    #reads the values from .env file and sets the encoding to utf-8
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()

