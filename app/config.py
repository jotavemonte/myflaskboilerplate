import os

from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')


class BaseConfig:
    DEBUG = os.getenv('DEBUG') or False
    PORT = os.getenv('PORT') or 3000
    TESTING = os.getenv('TESTING') or False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY') or 'default_secret_key'
    DBNAME = os.getenv('DBNAME') or 'dummydbname'
    DBUSER = os.getenv('DBUSER') or 'dummyuser'
    DBPWD = os.getenv('DBPWD') or 'dummypassword'
    DBHOST = os.getenv('DBHOST') or 'localhost'
    DBPORT = os.getenv('DBPORT') or '5432'
    SQLALCHEMY_DATABASE_URI = f'postgresql://'
    SQLALCHEMY_DATABASE_URI += f'{DBUSER}:{DBPWD}@{DBHOST}:{DBPORT}/{DBNAME}'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'default secret key'


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'test secret key'
    SQLALCHEMY_DATABASE_URI = f'sqlite////temp/test.db'


env = os.getenv('FLASK_ENV')

if env == 'development':
    Config = DevelopmentConfig
elif env == 'production':
    Config = ProductionConfig
elif env == 'test':
    Config = TestConfig
else:
    Config = BaseConfig
