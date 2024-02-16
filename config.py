from datetime import timedelta


class Config(object):
    DEBUG = True
    SECRET_KEY = 'dev'
    JWT_SECRET_KEY = 'dev'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=12)
    ERROR_INCLUDE_MESSAGE = False

class ProdConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class LocalConfig(Config):
    MYSQL_USER = 'root'
    MYSQL_PASS = 'cpce1901'
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = '3306'
    MYSQL_DB = 'igledev'
    SQLALCHEMY_DATABASE_URI = f"mysql://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'This is a SECRET KEY for all PEOPLE #1q2w3e4r5t6y7u8i9o'

class TestConfig(Config):
    TESTING = True