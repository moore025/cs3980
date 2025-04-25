from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
import os


class MyConfig(BaseSettings):
    connection_string: str
    secret_key: str

    # print(os.system("pwd"))
    model_config = SettingsConfigDict(
        env_file="/Users/nickmoore/VSCode/CS3980/cs3980/final_project/api/.env"
    )


@lru_cache
def get_settings():
    return MyConfig()
