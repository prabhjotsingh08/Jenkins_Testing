# backend/app/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "MiniCI"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    REPO_BASE_PATH: str = "/tmp/ci_repos"
    AGENT_POLL_INTERVAL: int = 3  # seconds
    SMTP_HOST: str = "localhost"
    SMTP_PORT: int = 1025
    SLACK_WEBHOOK_URL: str = ""
    SECRET_TOKEN: str = "changeme"  # for simple webhook auth

settings = Settings()
