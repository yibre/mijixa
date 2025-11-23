from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Config(BaseSettings):
    app_name: str = "mijixa"
    debug: bool = False
    db_user: str = "postgres"
    db_password: str = ""
    db_name: str = "mijixa2025.db"

    @property
    def db_url(self):
        return f"sqlite:///./{self.db_name}"


config = Config()