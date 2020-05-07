class ConfigFactory:
    def get(self, env):
        if env == 'development':
            return DevelopmentConfig()
        elif env == 'testing':
            return TestingConfig()
        else:
            return ProductionConfig()


class Config(object):
    DEBUG = False
    TESTING = False
    STORAGE = 'db'
    SWAGGER_URL = '/docs'
    API_DOCS_URL = '/static/swagger.json'


class DevelopmentConfig(Config):
    """ Configuration used during development """
    DEBUG = True
    STORAGE = 'db'
    MONGODB_SETTINGS = {
        'host': 'mongodb://db:27017/via'
    }


class TestingConfig(Config):
    """ Configuration used in tests"""
    DEBUG = True
    TESTING = True
    STORAGE = 'db'
    MONGODB_SETTINGS = {
        'host': 'mongodb://db:27017/test'
    }


class ProductionConfig(Config):
    """ Configuration used for production"""
    pass
