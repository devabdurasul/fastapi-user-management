from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET: str = "456456"
    DATABASE_URL: str = "sqlite+aiosqlite:///./test.db"  # Use the aiosqlite driver

    class Config:
        env_file = ".env"


settings = Settings()
