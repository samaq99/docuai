from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    secret_key: str
    qdrant_host: str = "localhost"
    openrouter_api_key: str
    base_url: str
    model_name: str

    qdrant_port: int = 6333
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    langfuse_public_key: str
    langfuse_secret_key: str
    langfuse_host: str = "http://localhost:3000"

    class Config:
        env_file = ".env"

settings = Settings()