import os
from typing import List, Type

basedir = os.path.abspath(os.path.dirname(__file__))

version = "v0.1"

class BaseConfig:
    CONFIG_NAME = "base"
    USE_MOCK_EQUIVALENCY = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "dev"
    SECRET_KEY = os.getenv(
        "DEV_SECRET_KEY", "Invalid key"
    )
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///{0}/app-dev.db".format(basedir)




EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig,
]
config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}
