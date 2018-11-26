import os
basedir = os.path.abspath(os.path.dirname(__file__))


class config:
    VALID_URL = ['/login',]
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is a secret string'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:soup@58.87.70.179:3306/lottery'


class TestingConfig(config):
    pass


class OpentingConfig(config):
    pass


class ProductionConfig(config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'open': OpentingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}