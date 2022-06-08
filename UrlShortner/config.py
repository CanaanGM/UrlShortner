from pydantic import BaseSettings

class Settings(BaseSettings):
    env_name :str = "Dev"
    db_url:str = "sqlite:///./shortener.db"

    class Config:
        env_file = ".env"


def get_settings() -> Settings:
    settings = Settings()
    print(f"settings for: {settings.env_name}")
    return settings