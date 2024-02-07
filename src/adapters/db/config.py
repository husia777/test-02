from functools import lru_cache
import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    postgres_user: str = os.environ.get('POSTGRES_USER')
    postgres_db: str = os.environ.get('POSTGRES_DB')
    postgres_password: str = os.environ.get('POSTGRES_PASSWORD')
    sqlalchemy_database_url: str = os.environ.get('SQLALCHEMY_DATABASE_URL')
    jwt_secret: str = os.environ.get('JWT_SECRET')
    jwt_algorithm: str = 'HS256'
    jwt_expires_s: int = 3600
    mail_host: str = os.environ.get('MAIL_HOST')
    mail_username: str = os.environ.get('MAIL_USERNAME')
    mail_password: str = os.environ.get('MAIL_PASSWORD')
    mail_port: str = os.environ.get('MAIL_PORT')
    mail_tls: str = os.environ.get('MAIL_TLS')
    mail_ssl: str = os.environ.get('MAIL_SSL')


@lru_cache
def get_settings():
    app_settings = Settings()
    return app_settings


settings = get_settings()
