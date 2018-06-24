import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://murungi:murungi1@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/images'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # CRSF_SECRET_KEY =os.environ.get("SECRET_KEY")
    CRSF_SECRET_KEY = 'x17M\xeacL>|i\xfa\x91\xcey,\x159\x01\xca2\x8a\x8dl\xd9'

class ProdConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://murungi:murungi1@localhost/pitch'
    DEBUG = True

class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://murungi:murungi1@localhost/pitch_test'
    pass
config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    }