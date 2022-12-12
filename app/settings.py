from abc import ABC
from functools import lru_cache
from logging import getLogger

from pydantic import BaseSettings


logger = getLogger("settings")

SETTINGS_PREFIX = 'pharm_'

class ServiceSettingsBase(BaseSettings, ABC):
    class Config:
        env_prefix = SETTINGS_PREFIX
        env_file = ".env"
        allow_mutation = False


class Settings(ServiceSettingsBase):
    telegram_token: str


@lru_cache()
def get_settings() -> Settings:
    logger.info("Settings created")
    settings = Settings()
    return settings
