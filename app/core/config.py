from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET: str = "456456"
    DATABASE_URL: str = "sqlite+aiosqlite:///./mydb.db"

    class Config:
        env_file = ".env"


settings = Settings()
