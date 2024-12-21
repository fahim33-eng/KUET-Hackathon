from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/kitchen_buddy"
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Kitchen Buddy"

    class Config:
        env_file = ".env"

settings = Settings() 