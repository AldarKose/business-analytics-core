from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    project_name: str = "Business Analytics Core"
    environment: str = "development"
    database_url: str
    api_key: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
