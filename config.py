# Add your configuration here


class Config(object):
    NAME = 'clampdown'
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    NAME = 'clampdown'


class DevelopmentConfig(Config):
    NAME = 'clampdown'
    DEBUG = True


class TestingConfig(Config):
    NAME = 'clampdown'
    TESTING = True
