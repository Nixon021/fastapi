from pydantic import BaseSettings


class Settings(BaseSettings):
    sever_host: str = '127.0.0.1'
    server_port: int = 8000
    debug: bool = True


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
