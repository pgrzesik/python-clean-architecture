import os


class Config:
    APP_DIR = os.path.abspath(os.path.dirname(__name__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))


class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True


class TestConfig(Config):
    ENV = 'test'
    TESTING = True
    DEBUG = True
