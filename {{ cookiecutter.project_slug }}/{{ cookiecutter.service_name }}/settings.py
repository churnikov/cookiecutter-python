from pydantic import BaseSettings, Field


class Settings(BaseSettings):

    env = Field("development", env="ENV")
    component_name = Field("{{ cookiecutter.project_slug }}", env="COMPONENT_NAME")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
